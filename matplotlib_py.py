import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv', names=['sepal length','sepal width','petal length','petal-width','class'])
print(iris.head())
fig, ax = plt.subplots()
  

ax.scatter(iris['sepal length'], iris['sepal width'])  
ax.set_title('Iris Dataset') 
ax.set_xlabel('sepal_length') 
ax.set_ylabel('sepal_width')
plt.show()