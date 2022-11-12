import pandas as pd
import numpy as np

def count(data):
  return len(data)

def mean(data):
  return np.sum(data)/len(data)

def std(data):
  return (np.sum((data-mean(data))**2)/(len(data)-1))**0.5

def min(data):
  return np.min(data)

def max(data):
  return np.max(data)


data=pd.read_csv("iris.csv",delimiter=",")
print(data.head(5))

df=pd.DataFrame(columns=['sepal_length','sepal_width','petal_length','petal_width'])

def create_df(data,df):
  for i in df.columns:
    df.loc['count',i]=count(data[i])
    df.loc['mean',i]=mean(data[i])
    df.loc['std',i]=std(data[i])
    df.loc['min',i]=min(data[i])
    df.loc['max',i]=max(data[i])
  return df

df=create_df(data,df)
print(df)

'''
df=pd.DataFrame(data,columns=['sepal_length','sepal_width','petal_length','petal_width']).describe()
df.drop(['25%','50%','75%'],axis=0,inplace=True)
print(df)
'''















