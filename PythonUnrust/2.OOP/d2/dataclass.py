from dataclass import dataclass, field
from enum import Enum

class Side(Enum):
    buy = "BUY",
    sell = "SELL"

print(Side.buy, Side.buy.name, Side.buy.value) #Side.BUY BUY buy
print(Side("sell")) #look up value = Side.sell


@dataclass
class Order:
    order_id: int
    price: int
    qty:int
    side: Side
    filled: int = 0


@dataclass (frozen =True) #immutable and cant be changed
class Point:
    x:int
    y:int

@dataclass 
class Basket:
    items: list[str] = field(default_factory = list) # a fresh list for each basket


@dataclass 
class Checked:
    qty:int
    def __post_init__(self):
        if self.qty <= 0:
            raise ValueError("qty must be positive")



