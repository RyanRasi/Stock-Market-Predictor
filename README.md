# Stock-Market-Predictor

A stock market predictor in Python that uses long short term memory for its judgements.

Run with...

```
python3 main.py
```

This stock market predictor will have the following features:

- [ ] Utilise financial data from AlphaAdvantage
- [ ] Use training and testing data to predict accurately
- [ ] Hopefully work well

Time series modelling is nothing new within stocks as it looks at the price history and attempts to predict what the future prices will be. However as most people know, stocks are volatile and whilst some tactics such as reading current events and the news helps, a lot of stock movement is sometimes down to random chance.

The stock that is focussed on in this program is Apple Inc.(AAPL)
This was mainly chosen due to its main foothold as one of the most profitable companies in the world as well as it can be predicted easily due to there being a product announcement every year in September which usually raises the stock.

It should be noted that the COVID-19 Worldwide Pandemic has affected stocks in quite a large manner with most stocks tanking for a few weeks and then some raising to the highest that they've been with others at historical lows. Due to this the model may be affected.

The reason I've decided to start this project was due to a great fascination of mine within the financial markets. I've also been to business school, where I've gained expereince in the Bloomberg terminal and have various diplomas and certificates within finance which makes this a journey that I'd love to give a shot and pursue.

The mid price is used for this program, this means that finding out the value of the stock is less important as it is more about finding out if the stock is going up or down.

How to use...

Firstly the user can enter any stock ticker of their choosing, the data will be retrieved and then the user will be prompted if they want to analyse the mid price data recieved and then start to train the model.
