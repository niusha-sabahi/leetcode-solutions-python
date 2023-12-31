# You are given an array 'prices' where 'prices[i]' is the price of a given stock on the ith day.
# Return the maximum profit you can achieve from choosing a day to buy one stock and choosing a different day in the 
# future to sell that stock, and repeating this process through the days in the list. You are allowed to buy then sell 
# your stock on the same day and vice versa. If you cannot achieve any profit, return 0.

# -- Performance At Time Of Completion --
# Runtime : Beats 94.74% of users with Python3 - GREEN
# Memory : Beats 65.15% of users with Python3 - GREEN

def maxProfit(prices):
    total_profit = 0

    for i in range (len(prices)-1):
        total_profit += max( prices[i+1] - prices[i], 0)
    return total_profit

print(maxProfit([1,2,3,4,5])) # expected output : 4
print(maxProfit([7,1,5,3,6,4])) # expected output : 7