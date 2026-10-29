"""Week 1 DSA functions, collected for testing."""

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    """Return the kth largest value using a min-heap of size k."""
    heap: list[int] = []  
    for n in nums:
        heapq.heappush(heap, n) 
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def longest_unique_run(prices: list[int]) -> int:
    """Length of the longest contiguous run with no repeated price."""
    last_seen: dict[int, int] = {}
    start = 0
    best = 0
    for i, p in enumerate(prices):
        if p in last_seen and last_seen[p] >= start:
            start = last_seen[p] + 1
        last_seen[p] = i
        best = max(best, i - start + 1)
    return best


def count_target_runs(pnl: list[int], k: int) -> int:
    """Count contiguous runs of days whose total is exactly k."""
    seen: dict[int, int] = {0: 1}
    total = 0
    runs = 0
    for p in pnl:
        total += p
        runs += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return runs


def zero_triples(qtys: list[int]) -> list[list[int]]:
    """All unique triples that sum to 0."""
    qtys = sorted(qtys)
    result: list[list[int]] = []
    for i in range(len(qtys) - 2):
        if i > 0 and qtys[i] == qtys[i - 1]:
            continue
        left, right = i + 1, len(qtys) - 1
        while left < right:
            total = qtys[i] + qtys[left] + qtys[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([qtys[i], qtys[left], qtys[right]])
                left += 1
                right -= 1
                while left < right and qtys[left] == qtys[left - 1]:
                    left += 1
    return result


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists into one sorted list using a heap."""
    heap: list[tuple[int, int, int]] = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    result: list[int] = []
    while heap:
        value, list_i, elem_i = heapq.heappop(heap)
        result.append(value)
        next_i = elem_i + 1
        if next_i < len(lists[list_i]):
            heapq.heappush(heap, (lists[list_i][next_i], list_i, next_i))
    return result