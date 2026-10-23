#List comprehension: [expression for item in iterable]
prices = [101, 99, 105, 98, 110, 97]
doubled = [p*2 for p in prices]

above_100 = [p for p in prices if p > 100]

#Dict comprehension: {key: value for}
squares = {n: n * n for n in range(5)}

#Set comprehension 
evens = {p %2 for p in prices}

#enumerate: gives(index, value) pairs
for i, p in enumerate(prices):
    print(i,p)

#sorted with key=: sort by something computed from each item
words = ["bb", "a", "ccc"]
print(sorted(words, key=len)) #sort by length of string
print(sorted(words, key=len, reverse= True))

#lambda function
pairs = [("x",3), ("y", 1), ("z", 2)]
print(sorted(pairs, key= lambda pair:pair[1]))