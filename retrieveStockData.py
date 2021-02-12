from pandas_datareader import data
import pandas as pd
import datetime as dt
import urllib.request
import json
import os


def retrieveStockData(api_key, stockTicker):
    print("Stock selected is: " + stockTicker)
    currentDate = dt.datetime.now().strftime("%x").replace("/", "-")
    print("Retrieving stock history up until %s\n" % currentDate)

    # JSON file with all the stock market data for AAL from the last 20 years
    url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s" % (
        stockTicker, api_key)

    # Save data to this file
    file_to_save = 'stockMarketData_%s_%s.csv' % (
        stockTicker, currentDate)

    if not os.path.exists(file_to_save):
        with urllib.request.urlopen(url_string) as url:
            data = json.loads(url.read().decode())
            # Extract stock market data
            data = data['Time Series (Daily)']
            df = pd.DataFrame(columns=['Date', 'Low', 'High', 'Close', 'Open'])
            for k, v in data.items():
                date = dt.datetime.strptime(k, '%Y-%m-%d')
                data_row = [date.date(), float(v['3. low']), float(v['2. high']),
                            float(v['4. close']), float(v['1. open'])]
                df.loc[-1, :] = data_row
                df.index = df.index + 1
        print('Data saved to : %s' % file_to_save)
        df.to_csv(file_to_save)

    # If data is up to date already then alert user
    else:
        print('Stock history is already up to date.')
