import retrieveStockData

print("Stock Predictor V1\nAuthor - Ryan Rasi\nwww.github.com/ryanrasi\n")

# API KEY - 9EIFJBT9JKNJ5BS7
api_key = '9EIFJBT9JKNJ5BS7'

# Asks for stock ticker to analyse
stockTicker = ""

# Gets user input for stock ticker
while stockTicker == "":
    stockTicker = input(
        "Please enter the stock ticker for price history retrieval\n").upper()
    fileName = retrieveStockData.retrieveStockData(api_key, stockTicker)
    break
