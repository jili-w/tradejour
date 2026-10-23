
prices = [100,90,91,67,69]
bid, ask = 99.5, 100.5 #unpacked tuple
first, * rest = prices
print[f"spread = {ask - bid:.2f}, first = {first}, rest= {rest}"]

