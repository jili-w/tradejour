from dataclasses import dataclass
from collections.abc import Iterator


@dataclass 
class DNode:
    key: int
    value: int
    prev: "DNode | None" = None
    next: "DNode | None" = None

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.map: dict[int,DNode]  = {}
        self.head = DNode(0 , 0)
        self.tail = DNode(0 , 0)
        self.head.next = self.tail
        self.tail.next = self.head

    def _remove(self, node: DNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_back(self, node:DNode ) -> None:
        last = self.tail.prev
        node.prev = last
        node.next = self.tail
        last.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_to_back(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_to_back(node)
            return
        new_node = DNode(key, value)
        self._add_to_back(new_node)
        self.map[key] = new_node
        if len(self.map) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]


