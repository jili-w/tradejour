#1: Push the bid prices [98, 100, 97, 100, 99] onto a max-heap (negated), then pop them all, printing best to worst.
import heapq
import bisect


bid = []
for b in [98, 100, 97, 100, 99]:
    heapq.heappush(bid, -b)

while bid:
    print(-heapq.heappop(bid))

#2 Kth largest: write kth_largest(nums, k) using a heap 
# of size k. Don’t sort the whole list. 
# (Hint: a min-heap of the k largest values seen so far has the kth largest at its top.)

def kth_largest(nums,k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap, n)
    return heap[0]
#3: Merge k sorted lists: given [[1, 4, 7], [2, 5, 8], [3, 6, 9]], produce one sorted list using a heap of (value, list_index, element_index) tuples. 
# (A classic problem from your DSA days; heapq.merge exists, but write it yourself.)

given =  [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
heap = []
for index,lst in enumerate(given):
    heapq.heappush(heap, (lst[0], index, 0)) # [(1,0,0), (2,1,0), (3,2,0)]
result =[]
while heap:
    value, list_i, elem_i = heapq.heappop(heap) # value = 1  list_i = 0 elem_i = 0
    result.append(value)
    next_i = elem_i + 1 # next_i = 1
    if next_i < len(given[list_i]): #checks if the list the value just came from still has another element at position next_i
        heapq.heappush(heap, (given[list_i][next_i], list_i, next_i))  #given[0][1][0]  == push 4

#4: Keep a sorted list of ask price levels with bisect.insort as [101, 99, 105, 100] arrive. 
# After each insert, print the best ask and the top 2 levels.
prices = [101, 99, 105, 100]
asks = []
for p in prices:
    bisect.insort(asks, p)
    print(f"best ask: {asks[0]} top2: {asks[:2]} ")

#5: Stretch: a price can appear twice in exercise 1’s heap. Push (-price, order_id) tuples instead, so equal prices are tie-broken by arr


bid = []
for i, b in enumerate([98, 100, 97, 100, 99]):
    heapq.heappush(bid, (-b, i))

while bid:
    price, order = heapq.heappop(bid)
    print(f"price: {-price}, orderId: {order}")