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

from dataclasses import dataclass
from collections.abc import Iterator

@dataclass
class Node:
    value: int
    next: "Node | None" = None      # quotes: Node isn't fully defined yet at this point

class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size = 0

    def __iter__(self) -> Iterator[int]:
        node = self.head
        while node is not None:
            yield node.value         # hands back one value, then pauses until the next loop step
            node = node.next

    def __len__(self) -> int:
        return self.size

    def prepend(self, value: int) -> None:
        new_node = Node(value, self.head)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, value: int) -> None:
        new_node = Node(value)
        self.size +=1
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def __contains__(self, value: int) -> bool:
        return any(n== value for n in self)

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
