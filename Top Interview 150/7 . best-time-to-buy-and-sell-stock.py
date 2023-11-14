# You are given an array 'prices' where 'prices[i]' is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
# to sell that stock. Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

# -- Performance At Time Of Completion --
# Runtime : Beats 76.71% of users with Python3 - GREEN
# Memory : Beats 64.38% of users with Python3 - GREEN

def maxProfit(prices):
    if not prices or len(prices) == 1:
        return 0

    buy_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < buy_price:
            buy_price = price
        else:
            max_profit = max(max_profit, price - buy_price)

    return max_profit

print(maxProfit([7,1,5,3,6,4]))