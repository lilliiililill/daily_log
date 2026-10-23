# 2026.10.24
# best_time_to_buy.py

def max_profit(prices):

    if not prices:

        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:

        if price < min_price:

            min_price = price

        else:

            max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
