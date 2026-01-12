import pytest
from django.test import Client
from items.models import Item, Order
from decimal import Decimal


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def sample_item():
    return Item.objects.create(
        name="Test item",
        description='Test description',
        price=Decimal('9.99')
    )


@pytest.fixture
def sample_order(sample_item):
    order = Order.objects.create(total_price=Decimal('1.11'))
    order.items.add(sample_item)
    order.calculate_total_price()
    return order
