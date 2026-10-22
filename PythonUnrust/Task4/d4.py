import heapq
import bisect

#heapq a min heap in a plain list, smallest item at i = 0
asks = []
heapq.heappush(asks, 101)
heapq.heappush(asks, 99)
heapq.heappush(asks, 105)
print(asks[0]) #gives 99 O(1)
print(heapq.heappop(asks)) # 99  removed O(log n)

heapq.heapify(data := [5,1,4]) #turns existing list into a heap , O(n)
print(heapq.nsmallest(2,[5,1,4,2])) #[1,2]

# theres no max heap in python:store negative values
bids = []
for p in [98,100,97]:
    heapq.heappush(bids, -p)
print(-bids[0])   #would give 100

# tuples are compared item by item
tasks = []
heapq.heappush(tasks, (2,"b"))
heapq.heappush(tasks, (1,"a"))
print(heapq.heappop(tasks)) #(1,"a")

#bisect: binary search on an already Sorted list
levels = [97, 99, 101, 105]
print(bisect.bisect_left(levels, 101)) # 2 -> index whrere 101 is or would go
bisect.insort(levels,100) #insert, keeping it sorted
print(levels) # [97, 99, 100, 101, 105]