import cv2
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd
import time
loaded_model = pickle.load(open("model.sav", 'rb'))

train_genration = True


data = []


def detect_grid(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.blur(gray, (3, 3))
    gray = cv2.adaptiveThreshold(gray,200,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,0)
    contours, hierarchy = cv2.findContours(gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    grid = []
    for contour in contours:
        A1 = cv2.contourArea(contour)
        if A1 < 10000 and A1 > 1000:
            perimeter = cv2.arcLength(contour, True)
            if cv2.norm(perimeter**2/16- A1) < 300:
                x, y, w, h = cv2.boundingRect(contour)
                x, y, w, h = x+5, y+5, w-10, h-10
                object = np.array(cv2.mean(image[y:y+h,x:x+w])).astype(int)[:-1]
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                val = (50*y) + (10*x)
                object = np.append(object,val)
                grid.append(object)
    if(len(grid)>0):
        grid = np.asarray(grid)
        grid = grid[grid[:, -1].argsort()]
    return  image,grid
def classifiy_grid(grid):
    str = ""
    if(len(grid)==9):
        color = grid[:,0:3]
        prediction = loaded_model.predict(color)
        #print(prediction)
        for i in prediction:
            if i == 0:
                str+="F"
            elif i == 1:
                str+="U"
            elif i == 2:
                str+="R"
            elif i == 3:
                str+="L"
            elif i == 4:
                str+="B"
            elif i == 5:
                str+="D"
    return str,prediction
    
def main():

    vid = cv2.VideoCapture(0)
    
    while(True):

        ret, frame = vid.read()
        frame,grid = detect_grid(frame)
        if(len(grid)==9):
            c = grid[:,:3]
            for i in grid:
                c = i
                c[3] = 5
                data.append(c)
            
            time.sleep(0.2)
            
        cv2.imshow('frame', frame)

        if len(data) > 1000:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    vid.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    data = np.array(data)
    

    df = pd.DataFrame (data)
    filepath = 'yellow.xlsx'
    df.to_excel(filepath, index=False)
    
    print(data)