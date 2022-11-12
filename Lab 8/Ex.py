import pandas as pd
import numpy as np

df=pd.DataFrame({'numbers':[1,2,3],'colors':["red","white","blue"]})
df=pd.DataFrame({'numbers':[1,2,3],'colors':["red","white","blue"]},columns=['numbers','colors'])

df=pd.DataFrame(np.random.randn(5,3),columns=['N1','N2','N3'])

df=pd.DataFrame({"N1":[1,2,3,4],"N2":[4,3,2,1]})
L=[{"Name":"John","Last Name":"Smith"},
    {"Name":"Jane","Last Name":"Doe"}]
df=pd.DataFrame(L)

data=np.loadtxt("sample.txt",delimiter=",")

data=pd.read_csv("sample.txt",delimiter=",")

data=pd.read_csv("sample2.txt",delimiter=",")


df=pd.DataFrame(np.random.randn(10,3),columns=['N1','N2','N3'])
# print(df.head(5))
# print(df.tail(5))

# print(df[["N2","N3"]])