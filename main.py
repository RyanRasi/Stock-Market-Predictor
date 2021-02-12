import retrieveStockData


print("Stock Predictor V1\nAuthor - Ryan Rasi\nwww.github.com/ryanrasi\n")
# API KEY - 9EIFJBT9JKNJ5BS7
api_key = '9EIFJBT9JKNJ5BS7'

# Apple stock market prices
stockTicker = "AAPL"

retrieveStockData.retrieveStockData(api_key, stockTicker)
