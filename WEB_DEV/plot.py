import pandas as pd 
iris= pd.read_csv('iris.csv', names=['sepal lenght','sepal width','petal length','petal-width','class'])
print(iris.head())