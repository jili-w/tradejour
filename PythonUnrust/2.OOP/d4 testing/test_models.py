import pytest
from tradejour.models import Order, Side, OrderId, OrderType, Price


def test_new_order_status_unfilled() -> None:
    o = Order(OrderId(1), Side.BUY, Price(100), 10)
    assert o.filled == 0
    assert o.remaining() == 10

def test_overfill_raises() -> None:
    o = Order(OrderId(1), Side.BUY, Price(100), 10)
    with pytest.raises(ValueError, match = "overfill"): #passes only if this error is raised
        o.fill(11)


@pytest.fixture
def order() -> Order:
    return Order(OrderId(1), Side.BUY, Price(100), 10)


def test_partial_fill(order:Order) -> None:
    order.fill(4)
    assert order.remaining() == 6

#Parametrize runs one test several times with different inputs. Instead of copying a test three times with different numbers, you list the inputs:
@pytest.mark.parametrize("amount,left" ,[(1, 9), (5, 5), (10, 0)] )
def test_fill_amounts(order:Order, amount:int, left: int) -> None:
    order.fill(amount)
    assert order.remaining() == left

def test_full_fill(order: Order) -> None:
    order.fill(10)
    assert order.is_filled()

def test_fills(order: Order) -> None:
    order.fill(3)
    order.fill(4)
    assert order.fills == [3,4]

def test_remaining_value(order: Order) -> None:
    order.fill(4)
    assert order.remaining_value() == 600

#a fill of 0, a negative fill, and an overfill after a partial fill (fill 6, then try 5).
def test_zero_fill(order: Order) -> None:
    with pytest.raises(ValueError, match="Fill has to be positive"):
        order.fill(0)

def test_negative_fill(order: Order) -> None:
    with pytest.raises(ValueError, match= "Fill has to be positive" ):
        order.fill(-1)

def test_over_after_partial_fill(order: Order) -> None:
    order.fill(6)
    with pytest.raises(ValueError, match = "overfill"):
        order.fill(5)
    assert order.remaining() == 4

#: qty 0, price −5 and filled=11 should each raise ValueError when the order is created. 
# Then write a separate test showing a market order at price 0 is accepted.
@pytest.mark.parametrize ("qty, price, filled",[
    (100, 0, 0),
    (-5, 10, 0),
    (100, 10, 11),
])
def test_invalid_orders(price: int, qty:int, filled:int) -> None:
    with pytest.raises(ValueError):
        Order(OrderId(1), Side.BUY, Price(price), qty, filled = filled)

def test_market_order() -> None:
    o = Order(OrderId(1), Side.BUY, Price(0), 5, order_type = OrderType.MARKET)
    assert o.order_type == OrderType.MARKET