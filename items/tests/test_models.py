import pytest
from decimal import Decimal
from items.models import Item, Order, OrderItem


@pytest.mark.django_db
def test_item_creation():
    item = Item.objects.create(
        name="Ноутбук",
        description='Мощный ноутбук',
        price=Decimal("999.99")
    )
    assert item.name == 'Ноутбук'
    assert item.description == "Мощный ноутбук"
    assert item.price == Decimal("999.99")


@pytest.mark.django_db
def test_order_calculation(sample_item):
    order = Order.objects.create()
    OrderItem.objects.create(order=order, item=sample_item, quantity=2)
    total = order.calculate_total_price()
    expected = sample_item.price * 2
    assert total == expected
    assert order.total_price == expected


@pytest.mark.django_db
def test_orderitem_subtotal(sample_item):
    order = Order.objects.create()
    quantity = 3
    order_item = OrderItem.objects.create(
        order=order,
        item=sample_item,
        quantity=quantity
    )
    actual_result = order_item.subtotal()
    expected_result = sample_item.price * quantity
    assert actual_result == expected_result