# You are given an array 'prices' where 'prices[i]' is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a day to buy one stock and choosing a different day in the future 
# to sell that stock, and repeating this process through the days in the list. Return the maximum profit you can 
# achieve from this series of transactions. If you cannot achieve any profit, return 0.

# -- Performance At Time Of Completion --
# Runtime : Beats % of users with Python3 - GREEN
# Memory : Beats % of users with Python3 - GREEN

def maxProfit(prices):
    if not prices or len(prices) == 1:
        return 0

    buy_price = prices[0]
    current_profit = 0
    total_profit = 0

    for price in prices[1:-1]:
        if price < buy_price:
            buy_price = price
        elif (price > buy_price) and ((price - buy_price) > current_profit):
            current_profit = price - buy_price
        else:
            total_profit = total_profit + current_profit
            current_profit = 0
            buy_price = price
    if (prices[-1] - buy_price) > current_profit:
       total_profit = total_profit + (prices[-1] - buy_price)
    return total_profit

# test text

print(maxProfit([1,2,3,4,5])) # 4
print(maxProfit([7,1,5,3,6,4])) # 7