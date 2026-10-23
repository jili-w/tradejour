#2. Three orders that net to zero (sort plus two pointers; LeetCode 15, “3Sum”)

#iven signed order quantities (positive is a buy, negative a sell), return all unique triples that sum to 0.

def zero_triples(qtys: list[int]) -> list[list[int]]:
    qtys = sorted(qtys) #[-4,-1,-1,0,1,2]
    result = []
    for i in range(len(qtys)-2): # 0 to 4
        if i > 0 and qtys[i] == qtys[i-1]:
            continue
        left, right = i + 1, len(qtys) - 1 # left = 1 right= 5
        while left < right :  
            total = qtys[i] + qtys[left] + qtys[right] #-4 - 1 +2 = -3
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([qtys[i], qtys[left], qtys[right]])
                left += 1
                right -= 1
                while left  < right and qtys[left] == qtys[left - 1]:
                    left += 1
    return result
assert zero_triples([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]