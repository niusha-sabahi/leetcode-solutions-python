prices = [7,1,4,6,1,5,7,3,1]

buy_price = min(prices)
sell_price = max(prices[prices.index(buy_price):])

print(prices.index(buy_price))
prices.remove(1)
print(prices)
print(prices.index(buy_price))
