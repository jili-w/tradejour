from dataclasses import dataclass,field
from enum import Enum
from typing import NewType
import heapq

class Side(Enum):
    BUY = "buy"
    SELL = "sell"

class OrderType(Enum):
    LIMIT = "limit"
    MARKET = "market"

OrderId = NewType("OrderId" , int)
Price = NewType("Price", int)

class OrderError(ValueError):
    """Base class for all order problems."""

class OverfillError(OrderError):
    """A fill larger than the remaining quantity."""

class InvalidOrderError(OrderError):
    """An order created with bad values."""

@dataclass 
class Order:
    order_id: OrderId
    side: Side
    price: Price
    qty: int
    order_type: OrderType = OrderType.LIMIT
    filled: int = 0
    fills: list[int] = field(default_factory = list)

    def remaining(self) -> int:
        return self.qty - self.filled

    def fill(self, amount: int) -> None:
        if amount > self.remaining():
            raise OverfillError("overfill")
        if amount <= 0:
            raise InvalidOrderError("Fill has to be positive")
        self.filled += amount
        self.fills.append(amount)

    def is_filled(self) -> bool:
        return self.remaining() == 0

    def remaining_value(self) -> int:
        return self.remaining() * self.price


    def __post_init__(self) -> None:
        if self.qty <= 0:
            raise InvalidOrderError("No Quantity")
        if self.filled < 0 or self.filled > self.qty:
            raise InvalidOrderError("Orders must be within quantity limits")
        if self.order_type != OrderType.MARKET and self.price <= 0:
            raise InvalidOrderError("Limit orders must be positive")
        if self.filled != sum(self.fills):
            raise InvalidOrderError("Contradictory Fills")


def cancel(book: dict[OrderId, Order], order_id:OrderId) -> None:
    print(f"cancelling {order_id}")
    book.pop(order_id, None)

