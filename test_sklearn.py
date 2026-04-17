"""train_test_split()"""

### This function used to train and test the model for the data
from sklearn.model_selection import train_test_split
X = [1,2,3,4,5]
Y = ['A','B','C','D','E']
X_train , X_test ,Y_train , Y_test = train_test_split(X,Y,test_size = 0.4)
print("X_train: ",X_train)
print("X_test: ",X_test)
print("Y_train: ",Y_train)
print("Y_test: ",Y_test)

"""With random state fixed"""
from sklearn.model_selection import train_test_split

X = [1, 2, 3, 4, 5]
y = ["A", "B", "C", "D", "E"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=3
)

print(X_train)   # always same
print(X_test)    # always same

"""With numpy array"""
import numpy as np
from sklearn.model_selection import train_test_split
X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([10,20,30,40,50])

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.4)
print("X_train: ",X_train)
print("X_test: ",X_test)
print("Y_train: ",Y_train)
print("Y_test: ",Y_test)

"""With pandas"""
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    "temp": [30, 32, 33, 35, 40],
    "humidity": [45, 50, 55, 40, 20],
    "risk": ["Low", "Low", "Medium", "Medium", "High"]
})

X = data[["temp", "humidity"]]
y = data["risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=1
)

print("Training Data:")
print(X_train)
print(y_train)

print("\nTesting Data:")
print(X_test)
print(y_test)

"""RandomForestClassifier"""
# It is a machine learning algorithem used for classification and reagression
"""import RandomForestClassifier"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
X = [1,2,3,4,5]
Y = ['A','B','C','D','E']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2)
print("X_test",X_train)
print("X_test",X_test)
print("Y_train",Y_train)
print("Y_test",Y_test)

model = RandomForestClassifier()
model.fit(X_train,Y_train)
pred = model.predict(Y_test,Y_test)

