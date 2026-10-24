#Rewrite yesterday’s Order as a dataclass with a Side enum, and keep your fill(),
#  is_filled() and remaining_value() methods. Compare the line count with yesterday’s version.

from dataclasses import dataclass,field
from enum import Enum

class Side(Enum):
    BUY = "buy"
    SELL = "sell"

class OrderType(Enum):
    LIMIT = "limit"
    MARKET = "market"

@dataclass 
class Order:
    order_id: int
    side: Side
    price: int
    qty: int
    order_type: OrderType = OrderType.LIMIT
    filled: int = 0
    fills: list[int] = field(default_factory = list)

    def remaining(self) -> int:
        return self.qty - self.filled

    def fill(self, amount: int) -> None:
        if amount > self.remaining():
            raise ValueError("overfill")
        if amount <= 0:
            raise ValueError("Fill has to be positive")
        self.filled += amount
        self.fills.append(amount)

    def is_filled(self) -> bool:
        return self.remaining() == 0

    def remaining_value(self) -> int:
        return self.remaining() * self.price

    def __post_init__(self):
        if self.qty <= 0:
            raise ValueError("No Quantity")
        if self.filled < 0 or self.filled > self.qty:
            raise ValueError("Orders must be within quantity limits")
        if self.order_type != OrderType.MARKET and self.price <= 0:
            raise ValueError("Limit orders must be positive")
        if self.filled != sum(self.fills):
            raise ValueError("Contradictory Fills")


#Make a frozen Trade dataclass: buy_id, sell_id, price, qty. 
# Try changing trade.qty and read the error. Then put two trades in a set. Why does that work for a frozen dataclass but not for a normal one?
@dataclass (frozen =True)
class Trade:
    buy_id: int
    sell_id: int
    price: int
    qty: int


t1 = Trade(1,1,100,10)
t2 = Trade(1,2,100,10)
# t1.qty = 5
trades = set()
trades.add(Trade(1, 1, 100, 10))
print(len(trades))
trades.add(t1)
print(len(trades))
trades.add(t1)
trades.add(t2)
print(Side.BUY == "buy")




    


