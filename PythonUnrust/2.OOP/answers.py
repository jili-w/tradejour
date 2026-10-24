#Type out the Order class and create three orders. Print them to check that __repr__ works.

class Order:
    def __init__(self, order_id: int , side: str, price:int ,  qty: int) -> None:
        self.order_id = order_id
        self.price = price
        self.qty = qty
        self.side = side

    def fill(self,amount: int) -> None:
        if self.qty < amount:
            raise ValueError("overfill")
        if amount <= 0:
            raise ValueError("Fill amount must be positive")
        self.qty -= amount
        

    def is_filled(self) -> bool:
        return self.qty == 0

    def __repr__(self) -> str:
        return f"Order:{self.order_id}, side:{self.side} price: {self.price} quantity: {self.qty}"
    #Add __eq__ (same order_id means equal) and test it: two separate Order(1, ...) objects should be ==, and an Order(2, ...) shouldn’t be.

    def __eq__(self, other) -> bool:
        return self.order_id == other.order_id
    #Add a remaining_value() method that returns price * qty.

    def remaining_value(self) -> int:
        return self.price * self.qty

    #Add __lt__ so that a list of ask orders sorts by price, then order_id: price-time priority again, now built into the class. 
    # Then sorted(asks) and heapq.heappush will just work with Order objects. (Hint: tuples compare item by item, so __lt__ can compare two tuples.)

    def __lt__(self,other) -> bool:
        return (self.price,self.order_id) < (other.price,other.order_id)




o = Order(101, "buy", 100, 20)
print(o)