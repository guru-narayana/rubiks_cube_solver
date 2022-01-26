from cgi import test
from numpy import array
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle

dataframe1 = pandas.read_excel("E:/semester_work/Digital Image Processsing/Project/green.xlsx")
dataframe2 = pandas.read_excel("E:/semester_work/Digital Image Processsing/Project/white.xlsx")
dataframe3 = pandas.read_excel("E:/semester_work/Digital Image Processsing/Project/red.xlsx")
dataframe4 = pandas.read_excel("E:/semester_work/Digital Image Processsing/Project/orange.xlsx")
dataframe5 = pandas.read_excel("E:/semester_work/Digital Image Processsing/Project/blue.xlsx")
dataframe6 = pandas.read_excel("E:/semester_work/Digital Image Processsing/Project/yellow.xlsx")
frames = [dataframe1,dataframe2,dataframe3,dataframe4,dataframe5,dataframe6]

result = pandas.concat(frames).sample(frac=1)
array = result.values

X = array[:,0:3]
Y = array[:,3]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
print(X_train.shape)
# Fit the model on training set
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# save the model to disk
filename = 'rgb_model.sav'
pickle.dump(model, open(filename, 'wb'))


# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
#print(result)
