#1. Rewrite your price-changes loop from Day 2 as a one-line list comprehension.

prices = [101, 99, 105, 98, 110, 97]

# changes = []

# for today, tommorow in zip(prices, prices[1:]):
#     changes.append(tommorow - today)

changed_prices = [tommorow - today for today, tommorow in zip(prices,prices[1:])]

#this gives [-2, 6, -7, 12, -1]

#2. From prices, make a list of only the down days: the changes that are negative.

down_days = [p for p in changed_prices if p < 0]

#3. Use enumerate to print each price with its day number starting from 1, like Day 1: 101. (Hint: enumerate has an optional second argument.)

for i, p in enumerate(prices, start=1):
    print(f"Day {i}: {p}.")

#4 Given trades = [("AAPL", 10), ("MSFT", 5), ("TSLA", 20), ("NVDA", 2)], sort them by quantity, largest first.
trades = [("AAPL", 10), ("MSFT", 5), ("TSLA", 20), ("NVDA", 2)]

by_quantity = sorted(trades, key = lambda t:t[1]  ,reverse = True)

#5 Build a dict comprehension that maps each ticker in trades to its quantity. Then build one that only includes trades with quantity 5 or more.
trade_dict = {t:qty for t,qty in trades}
five_or_more = {t:qty for t,qty in trades if qty >= 5 }

#6 Using enumerate, find the day number of the highest price without using .index(). One way is max with key= over the enumerate pairs.
numbered = list(enumerate(prices,start= 1))
day, price = max(numbered, key= lambda n:n[1] )
