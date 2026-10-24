class Order:
    def __init__ (self, order_id: int, side: str, price: int, qty: int):
        self.order_id = order_id
        self.side = side
        self.price = price
        self.qty = qty

    def fill(self, ammount: int) -> None:
        self.qty -= ammount

    def is_filled(self) -> bool:
        return self.qty == 0

    def __repr(self) -> str:
        return f"Order(id= {self.order_id})"

    def __eq__(self, other) -> bool: # makes == work as intended
        return self.order_id == other.order_id

    def __lt__(self, other) -> bool: #makes < work and by proxy sorted(), min(), heapq
        return  self.price < other.price

o = Order(1, "buy", 100, 10)
print(o)
o.fill(4)
print(o.qty, o.is_filled())