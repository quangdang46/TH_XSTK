import pandas as pd
import numpy as np


data=pd.read_csv('population.csv',delimiter=',')
print(data.head(5))

def count(data):
  return len(data)

def mean(data):
  return np.mean(data)

def std(data):
  return np.sum((data - np.mean(data))**2) / len(data)

def min(data):
  return np.min(data)

def max(data):
  return np.max(data)

# 'Country Name', 'Country Code','Mean','Std','Min','Max'

df=pd.DataFrame(data,columns=['Country Name', 'Country Code','Mean','Std','Min','Max'])
df['Mean']=data.groupby(['Country Name','Country Code'])['Year'].transform(mean)
df['Std']=data.groupby(['Country Name','Country Code'])['Year'].transform(std)
df['Min']=data.groupby(['Country Name','Country Code'])['Year'].transform(min)
df['Max']=data.groupby(['Country Name','Country Code'])['Year'].transform(max)
df=df.drop_duplicates()

print(df)


