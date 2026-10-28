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