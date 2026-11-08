import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_json("Advertising.json")
df.info()
di=pd.DataFrame(df)
plt.scatter(di["TV"],di["Sales"],color="red")
plt.xlabel("Tv Ads Budget")
plt.ylabel("Sales")
plt.title("Tv Ads Budget vs Sales")
plt.show()