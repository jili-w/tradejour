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

    def __post_init__(self) -> None:
        if self.qty <= 0:
            raise ValueError("No Quantity")
        if self.filled < 0 or self.filled > self.qty:
            raise ValueError("Orders must be within quantity limits")
        if self.order_type != OrderType.MARKET and self.price <= 0:
            raise ValueError("Limit orders must be positive")
        if self.filled != sum(self.fills):
            raise ValueError("Contradictory Fills")
