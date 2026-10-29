from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a")          # mark "a" most recent  → order is b, a
od.popitem(last=False)       # remove the OLDEST item → removes ("b", 2)


class LRUCacheOD:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.data: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        # missing → -1; otherwise mark as most recent, then return the value
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]


    def put(self, key: int, value: int) -> None:
        # set the value, mark as most recent, evict the oldest if over capacity
        self.data[key]  = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)

#Explain how a price level built as a doubly linked list, 
# plus a dict order_id → node, gives O(1) cancel, and why a deque can’t.
