def merge_sessions(windows: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    for start, end in sorted(windows):          # sorts by start, since lists compare item by item
        if merged and start <= merged[-1][1]:   # overlaps the last merged window
            merged[-1][1] = max(merged[-1][1], end)              # extend its end
        else:
            merged.append([start, end])               # a new window
    return merged

# [[1, 3], [2, 6], [8, 10], [15, 18]] -> [[1, 6], [8, 10], [15, 18]]
# [[1, 4], [4, 5]]                    -> [[1, 5]]   (touching counts as overlapping)
# []                                  -> []


def min_removals(windows: list[list[int]]) -> int:
    removal = 0
    last_end = float("-inf")
    for start, end in sorted(windows, key= lambda w: w[1]):
        if start >= last_end:
            last_end = end
        else:
            removal += 1
    return removal

# [[1, 2], [2, 3], [3, 4], [1, 3]] -> 1
# [[1, 2], [1, 2], [1, 2]]         -> 2
# [[1, 2], [2, 3]]                 -> 0


def remove_nth_from_end(self, n: int) -> None:
    dummy =  Node(0, self.head)
    fast = dummy
    slow = dummy
    for node in range(n + 1):
        fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next 
    slow.next = slow.next.next
    self.head = dummy.next
    self.size -= 1
