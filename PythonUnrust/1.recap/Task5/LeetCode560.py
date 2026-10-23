#Count P&L streaks hitting a target (hashmap with prefix sums; LeetCode 560, “Subarray Sum Equals K”)

#Given daily P&L values, count the contiguous runs of days whose total is exactly k.

def count_target_runs(pnl: list[int], k: int) -> int:
    seen = {0: 1}
    total = 0
    runs = 0
    for p in pnl: # 3
        total += p                 # update running total = 3
        runs += seen.get(total - k, 0)     # how many earlier totals equal total − k? runs = 0
        seen[total] = seen.get(total, 0) + 1           # record this total (count +1)  seen[3] = 
    return runs


assert count_target_runs([1, 1, 1], 2) == 2
assert count_target_runs([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4