
# 1.Given prices = [101, 99, 105, 98, 110, 97], print the daily changes 
# ([-2, 6, -7, 12, -1]). Hint: slicing plus zip.

# zip takes 2 or more sequences and walks them through in step 

prices = [101, 99, 105, 98, 110, 97]

changes = []

for today, tommorow in zip(prices, prices[1:]):
    changes.append(tommorow - today)

#2.Given a list of trades [("AAPL", 10), ("MSFT", 5), ("AAPL", -3)], build a dict of net position per ticker.

trades = [("AAPL", 10), ("MSFT", 5), ("AAPL", -3)]
position = {}

for tick, qty in trades:
    position[tick] = position.get(tick, 0) + qty

# 3.From orders = [3, 7, 3, 9, 7, 1], print the unique order IDs in sorted order.
orders = set([3, 7, 3, 9, 7, 1])

print(sorted(set(orders)))

#4.Swap two variables in one line without a temp variable.

# var1 ,var2 = var2, var1

#5.Print a small table of the dict from exercise 2, with tickers left-aligned and positions right-aligned.

for tickers, qty in position.items():
    print(f"{tickers:<6} {qty:>8}")
