import pytest
from django.urls import reverse
from items.models import Order


@pytest.mark.django_db
def test_item_detail_view(client, sample_item):
    url = reverse('item_detail', args=[sample_item.id])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_order_view_get(client, sample_item):
    url = reverse('create_order')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_order_view_post(client, sample_item):
    url = reverse('create_order')
    response = client.post(url, { 'items': [str(sample_item.id)]})

    assert response.status_code == 302
    assert Order.objects.count() == 1