import retrieveStockData
import dataAnalysis


print("Stock Predictor V1\nAuthor - Ryan Rasi\nwww.github.com/ryanrasi\n")
# API KEY - 9EIFJBT9JKNJ5BS7
api_key = '9EIFJBT9JKNJ5BS7'

# Asks for stock ticker to analyse
stockTicker = ""
while stockTicker == "":
    stockTicker = input(
        "Please enter the stock ticker for price history retrieval\n")
    fileName = retrieveStockData.retrieveStockData(api_key, stockTicker)
    break

decision = ""
while not decision == "1":
    decision = input(
        "\nDo you wish to analyse data or exit program? \n1. Analyse data.\n2. Exit Program\n")
    if decision == "1":
        dataAnalysis.analyse(fileName)
        break
    elif decision == "2":
        quit()
        break
