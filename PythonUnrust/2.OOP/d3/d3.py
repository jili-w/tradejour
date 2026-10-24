from models import Side, Order, OrderType
import heapq

##1
# def total_qty(orders: list[Order]) -> int:
#     total = sum(o.qty for o in orders)
#     return str(total)


# orders = [Order(1, Side.BUY, 100, 10), Order(2, Side.SELL, 101, 5)]
# print(total_qty(orders) + 1)

#2 None trap
book = {1: Order(1, Side.BUY, 100, 10), 2: Order(2, Side.SELL, 101, 5)}
def find_order(book: dict[int, Order], oid: int) -> Order | None:
    return book.get(oid)

order = find_order(book, 99)
if order is None:
    print("Not Found")
else:
    print(order.qty)

#3 merge k sorted list

def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    heap: list[tuple[int,int,int]] = []
    for i , p in enumerate(lists):
        if p:
            heapq.heappush(heap,(p[0],i , 0))
    result: list[int] = []
    while heap:
        value, index_i, elem_i = heapq.heappop(heap)
        result.append(value)
        next_i = elem_i + 1
        if next_i < len(lists[index_i]):
            heapq.heappush(heap, (lists[index_i][next_i], index_i, next_i))

    return result


assert merge_k_sorted([[1, 4, 7], [2, 5, 8], [3, 6, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert merge_k_sorted([[1, 2], [], [0, 5]]) == [0, 1, 2, 5]
assert merge_k_sorted([]) == []

