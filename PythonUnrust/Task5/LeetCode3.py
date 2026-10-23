#Longest stretch with no repeated price (sliding window plus a dict; LeetCode 3, “Longest Substring Without Repeating Characters”)

#Return the length of the longest contiguous run of prices where no price appears twice.

def longest_unique_run(prices: list[int]) -> int:
    seen = {}
    best = 0
    start = 0
    for i, p in enumerate(prices):  #(2, 101)
        if p in seen and seen[p] >= start: #if (101) was seen and seen[p] >= 0, which is true 
            start = seen[p] + 1   # start = 1
        seen[p] = i # seen[101] = 2
        best = max(i-start + 1,best) #   2-0 +1 = 2
    return best


assert longest_unique_run([101, 99, 101, 98, 97, 99, 100]) == 5
assert longest_unique_run([]) == 0