#Pandas
import pandas as pd
data={'Name':['Harman','Aarushi','Amrit'],'Age':[19,20,21],'MailId':['harmanpv@gmail.com','aarushi048@gmail.com','amrit89@gmail.com'],
      'PhoneNo':[8699081502,8427593494,9964457899]}
df=pd.DataFrame(data,index=[1,2,3])
print(df)
d=pd.read_csv("test1.csv")
df=pd.DataFrame(d)
print(df.head(5))
print(df.head(10))
print(df.axes)
print(df.T)
print(df.tail(5))
print(df['MinTemp'].head)
print(df['MinTemp'].dtypes)
print(df['MinTemp'].shape)