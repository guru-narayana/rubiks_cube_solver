import numpy as np
import cv2
from rubik_solver import utils
import keyboard
import serial
import time
from pyfirmata import ArduinoMega
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread("white.pngt")
#ARD = ArduinoMega("COM3")



def calculate():
  x = 100
  y = 100
  winName = 'DroidCam'
  cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
  cap = cv2.VideoCapture('http://localhost:4747/mjpegfeed?640x480')

  while (True):

      ret, frame = cap.read()
      ret, guru = cap.read()

      guru_ = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

      # Display the resulting frame
      cv2.imshow('frame', guru)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break









      guru_ = cv2.cvtColor(guru, cv2.COLOR_BGR2HSV)

      cv2.rectangle(frame, (x+25, y+25), (x + 75, y + 75), (0, 255, 0), 3)
    # 22
      cv2.rectangle(frame, (x + 125, y + 125), (x + 175, y + 175), (0, 255, 0), 3)
    # 33
      cv2.rectangle(frame, (x + 225, y + 225), (x + 275, y + 275), (0, 255, 0), 3)
    # 12
      cv2.rectangle(frame, (x + 125, y + 75), (x + 175, y+25), (0, 255, 0), 3)
    # 13
      cv2.rectangle(frame, (x + 225, y + 75), (x + 275, y+25), (0, 255, 0), 3)
    # 21
      cv2.rectangle(frame, (x+25, y + 125), (x + 75, y + 175), (0, 255, 0), 3)
    # 31
      cv2.rectangle(frame, (x+25, y + 225), (x + 75, y + 275), (0, 255, 0), 3)
    # 32
      cv2.rectangle(frame, (x + 125, y + 225), (x + 175, y + 275), (0, 255, 0), 3)
    # 23
      cv2.rectangle(frame, (x + 225, y + 125), (x + 275, y + 175), (0, 255, 0), 3)
    # Moving grid as required
      if keyboard.is_pressed('w'):
          y = y - 1
      if keyboard.is_pressed('s'):
          y = y + 1
      if keyboard.is_pressed('a'):
          x = x - 1
      if keyboard.is_pressed('d'):
          x = x + 1
      cv2.imshow("select the grid", frame)
      cv2.imshow("hsv", guru_)
  cap.release()
  cv2.destroyAllWindows()




  i = 0
  p = x+30
  q = y+30
  c11 = [0, 0, 0]
  while p < (x + 70):
        while q < (y + 70):

            c11 = c11 + guru_[p, q]

            i = i + 1
            q = q + 1
        p = p + 1
  a=c11
  a[0] = (a[0] / i)
  a[1] = (a[1] / i)
  a[2] = (a[2] / i)
  avg_c11 = a
  # 12
  p = x + 130
  q = y+30
  c12 = [0, 0, 0]
  i = 0
  while p < (x + 170):
        while q < (y + 70):
            c12 = c12 + guru_[p, q]
            i = i + 1
            q = q + 1
        p = p + 1

  avg_c12 = (c12 / i)

  # 13
  p = x + 230
  q = y+30
  c13 = [0, 0, 0]
  i = 0
  while p < (x + 270):
        while q < (y + 70):
            c13 = c13 + guru_[p, q]
            i = i + 1
            q = q + 1
        p = p + 1

  avg_c13 = (c13 / i)
  # 22
  p = x + 130
  q = y + 130
  c22 = [0, 0, 0]
  i = 0
  while p < (x + 170):
        while q < (y + 170):
            c22 = c22 + guru_[p, q]
            i = i + 1
            q = q + 1
        p = p + 1

  avg_c22 = (c22 / i)
  # 23
  p = x + 230
  q = y + 130
  c23 = [0, 0, 0]
  i = 0
  while p < (x + 270):
        while q < (y + 170):
            c23 = c23 + guru_[p, q]
            i = i + 1
            q = q + 1
        p = p + 1

  avg_c23 = (c23 / i)

  # 21
  p = x+30
  q = y + 130
  c21 = [0, 0, 0]
  i = 0
  while p < (x + 70):
        while q < (y + 170):
            c21 = c21 + guru_[p, q]
            i = i + 1
            q = q + 1
        p = p + 1

  avg_c21 = (c21 / i)
  # 31
  p = x+30
  q = y + 230
  c31 = [0, 0, 0]
  i = 0
  while p < (x + 70):
        while q < (y + 270):
            c31 = c31 + guru_[p, q]
            i = i + 1
            q = q + 1
        p = p + 1

  avg_c31 = (c31 / i)

  # 32
  p = x + 130
  q = y + 230
  c32 = [0, 0, 0]
  i = 0
  while p < (x + 170):
        while q < (y + 270):
            c32 = c32 + guru_[p, q]
            i = i + 1
            q = q + 1
        p = p + 1

  avg_c32 = (c32 / i)

  # 33
  p = x + 230
  q = y + 230
  c33 = [0, 0, 0]
  i = 0
  while p < (x + 270):
        while q < (y + 270):
            c33 = c33 + guru_[p, q]
            i = i + 1
            q = q + 1
        p = p + 1

  avg_c33 = (c33 / i)

  # display average color_value
  avg_c11 = avg_c11.astype(int)
  avg_c12 = avg_c12.astype(int)
  avg_c13 = avg_c13.astype(int)
  avg_c21 = avg_c21.astype(int)
  avg_c22 = avg_c22.astype(int)
  avg_c23 = avg_c23.astype(int)
  avg_c31 = avg_c31.astype(int)
  avg_c32 = avg_c32.astype(int)
  avg_c33 = avg_c33.astype(int)
  arr = (avg_c11, avg_c21, avg_c31, avg_c12, avg_c22, avg_c32, avg_c13, avg_c23, avg_c33)
  results=[0,1,2,3,4,5,6,7,8]
  print(avg_c11)
  print(avg_c21)
  print(avg_c31)
  print(avg_c12)
  print(avg_c22)
  print(avg_c32)
  print(avg_c13)
  print(avg_c23)
  print(avg_c33)

  #cv2.imshow("guru", guru)
  #cv2.imshow("guru hsv ", guru_)
  for i in results :
       #green
     if(60<arr[i][0]<85 and 100<arr[i][1]<260and 100<arr[i][2]<265):

        results[i]= "g"
     if (0 < arr[i][0] < 360 and 0 < arr[i][1] < 100 and 170< arr[i][2] < 265):
        results[i] = "w"
     if (90< arr[i][0] < 110 and 100 < arr[i][1] < 260 and 100 < arr[i][2] < 265):
        results[i] = "b"
     if (25< arr[i][0] < 45 and 100< arr[i][1] < 260 and 100 < arr[i][2] < 265):
        results[i] = "y"
     if (4 <= arr[i][0] < 20 and 100 < arr[i][1] < 260 and 100 < arr[i][2] < 265):
        results[i] = "o"
     if (0 <= arr[i][0] < 4 and 100 < arr[i][1] < 260 and 100 < arr[i][2] < 265):
        results[i] = "r"



  #print(results)
  return results
  def release():
      cv2.destroyAllWindows()
      cap.release()
  release()


while True:
    if keyboard.is_pressed("t"):
        text1 = calculate()
        print(text1)


    if keyboard.is_pressed("l"):
        text2 = calculate()
        print(text2)


    if keyboard.is_pressed("f"):
        text3 = calculate()
        print(text3)


    if keyboard.is_pressed("r"):
        text4 = calculate()
        print(text4)


    if keyboard.is_pressed("b"):
        text5 = calculate()
        print(text5)


    if keyboard.is_pressed("d"):
        text6 = calculate()
        print(text6)


    if keyboard.is_pressed("m"):
        cube = text1 + text2 + text3 + text4 + text5 + text6


        cube1=""
        for i in cube:
            cube1 = cube1+i
        print(cube1)
        solln = utils.solve(cube, 'CFOP')

        x = len(solln) - 1
        print(x)

        sollution = list()
        i = 0
        while i < x:
            if solln[i] != " ":

                if solln[i + 1] == "'" or solln[i + 1] == "2":

                    list.append(sollution, solln[i] + solln[i + 1])
                    i = i + 2
                else:
                    list.append(sollution, solln[i])
            i = i + 1
        list.append(sollution, solln[x - 1])
        print(sollution)

        for i in sollution:
            if (i == "U"): #top clockwise
                ARD.digital[2].write(1)
                for x in range(12):
                    ARD.digital[3].write(1)
                    time.sleep(0.01)
                    ARD.digital[3].write(0)
                    time.sleep(0.01)

            if (i == "U'"):  #top anticlockwise
                ARD.digital[2].write(0)
                for x in range(12):
                    ARD.digital[3].write(1)
                    time.sleep(0.01)
                    ARD.digital[3].write(0)
                    time.sleep(0.01)
            if (i == "U2"):
                ARD.digital[2].write(1)
                for x in range(24):
                    ARD.digital[3].write(1)
                    time.sleep(0.01)
                    ARD.digital[3].write(0)
                    time.sleep(0.01)
            if (i == "D"):
                ARD.digital[4].write(1)
                for x in range(12):
                    ARD.digital[5].write(1)
                    time.sleep(0.0005)
                    ARD.digital[5].write(0)
                    time.sleep(0.0005)
            if (i == "D'"):
                ARD.digital[4].write(0)
                for x in range(12):
                    ARD.digital[5].write(1)
                    time.sleep(0.0005)
                    ARD.digital[5].write(0)
                    time.sleep(0.0005)
            if (i == "D2"):
                ARD.digital[4].write(1)
                for x in range(24):
                    ARD.digital[5].write(1)
                    time.sleep(0.0005)
                    ARD.digital[5].write(0)
                    time.sleep(0.0005)
            if (i == "R"):
                ARD.digital[6].write(1)
                for x in range(12):
                    ARD.digital[7].write(1)
                    time.sleep(0.0005)
                    ARD.digital[7].write(0)
                    time.sleep(0.0005)
            if (i == "R'"):
                ARD.digital[6].write(0)
                for x in range(12):
                    ARD.digital[7].write(1)
                    time.sleep(0.0005)
                    ARD.digital[7].write(0)
                    time.sleep(0.0005)
            if (i == "R2"):
                ARD.digital[6].write(1)
                for x in range(24):
                    ARD.digital[7].write(1)
                    time.sleep(0.0005)
                    ARD.digital[7].write(0)
                    time.sleep(0.0005)
            if (i == "L"):
                ARD.digital[8].write(1)
                for x in range(12):
                    ARD.digital[9].write(1)
                    time.sleep(0.0005)
                    ARD.digital[9].write(0)
                    time.sleep(0.0005)
            if (i == "L'"):
                ARD.digital[8].write(0)
                for x in range(12):
                    ARD.digital[9].write(1)
                    time.sleep(0.0005)
                    ARD.digital[9].write(0)
                    time.sleep(0.0005)
            if (i == "L2"):
                ARD.digital[8].write(1)
                for x in range(24):
                    ARD.digital[9].write(1)
                    time.sleep(0.0005)
                    ARD.digital[9].write(0)
                    time.sleep(0.0005)
            if (i == "F"):
                ARD.digital[10].write(1)
                for x in range(12):
                    ARD.digital[11].write(1)
                    time.sleep(0.0005)
                    ARD.digital[11].write(0)
                    time.sleep(0.0005)
            if (i == "F'"):
                ARD.digital[10].write(0)
                for x in range(12):
                    ARD.digital[11].write(1)
                    time.sleep(0.0005)
                    ARD.digital[11].write(0)
                    time.sleep(0.0005)
            if (i == "F2"):
                ARD.digital[10].write(1)
                for x in range(24):
                    ARD.digital[11].write(1)
                    time.sleep(0.0005)
                    ARD.digital[11].write(0)
                    time.sleep(0.0005)
            if (i == "B"):
                ARD.digital[30].write(1)
                for x in range(12):
                    ARD.digital[31].write(1)
                    time.sleep(0.0005)
                    ARD.digital[31].write(0)
                    time.sleep(0.0005)
            if (i == "B'"):
                ARD.digital[30].write(0)
                for x in range(12):
                    ARD.digital[31].write(1)
                    time.sleep(0.0005)
                    ARD.digital[31].write(0)
                    time.sleep(0.0005)
            if (i == "B2"):
                ARD.digital[30].write(1)
                for x in range(24):
                    ARD.digital[31].write(1)
                    time.sleep(0.0005)
                    ARD.digital[31].write(0)

                    time.sleep(0.0005)
        print("completed")


    if keyboard.is_pressed('e'):
        break
