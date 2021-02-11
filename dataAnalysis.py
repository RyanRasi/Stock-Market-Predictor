import matplotlib.pyplot as plt
import pandas as pd

#Data from source
stockData = './stock_market_data-AAPL'

df = pd.read_csv (stockData+".csv")

# Sort DataFrame by date
df = df.sort_values('Date')

# Gets all of the rows
df.head()

#Plots figure
plt.figure(figsize = (18,9))
plt.plot(range(df.shape[0]),(df['Low']+df['High'])/2.0)
plt.xticks(range(0,df.shape[0],500),df['Date'].loc[::500],rotation=45)
plt.title(stockData.replace("./stock_market_data-", ""),fontsize=18)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Mid Price',fontsize=18)
plt.show()