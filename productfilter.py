import pandas as pd
i=pd.read_csv("products.csv")
print(i[["Product","Price"]])
print(i[(i["Category"]=="Electronics") & (i["Price"]>10000) & (i["Stock"]<10)])
print(i[(i["Category"]=="Electronics") | (i["Price"]>10000) | (i["Stock"]<10)])

