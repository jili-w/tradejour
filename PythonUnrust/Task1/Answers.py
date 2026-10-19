
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


