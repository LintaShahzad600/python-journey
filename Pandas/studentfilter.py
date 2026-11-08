import pandas as pd
data=pd.read_csv("students.csv")
print(data)
f=data.head(2)
print(f)
d=data.tail(2)
print(d)
data.info()
(print(data[["Name","Marks"]]))
print(data(data[["Department"] =="CS"]))

