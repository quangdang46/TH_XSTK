import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('iris.csv',delimiter=',')

# 1
plt.scatter(data['sepal_length'],data['sepal_width'])
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.show()
# 2
plt.hist(data['sepal_length'],bins=20)
plt.xlabel('sepal_length')
plt.ylabel('count')
plt.show()
