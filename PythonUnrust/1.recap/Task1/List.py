prices = [100,90,91,67,69]
prices.append(97)
print (prices[0], prices[-1]) #first and last (using a slice)
print(prices[1:4]) # 1 to 4
print(prices[::-1]) #reversed
print(sorted(prices), len(prices), max(prices))
