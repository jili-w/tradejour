from collections import deque ,defaultdict, Counter, OrderedDict


# a deque has fast remove/add at both ends (list is slow at front) double ended queue
q = deque()
q.append("ord1") # q = [ord1]
q.append("ord2") # q = [ord1,ord2]
q.appendleft("ord0") # q = [ord0,ord1,ord2]
print(q.popleft()) # remove from the front 
print(q[0],len(q)) # peek at front without removing

position = defaultdict(int)
position["AAPL"] += 10
levels = defaultdict(list)
levels[100].append("order1")
print(dict(position), dict(levels))

#counter 
sides = Counter(["buy", "sell", "sell","buy"])
print(sides) #Counter({'buy':2, 'sell':2})
print(sides.most_common(1)) #{'buy':2}


# remembers insertion order + can move keys around
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a") # now b,a
print(list(od))
