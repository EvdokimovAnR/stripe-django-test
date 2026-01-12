import stripe
from django.db import models



class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    items = models.ManyToManyField(Item, through='OrderItem', verbose_name='Товары')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая сумма')
    stripe_session_id = models.CharField(max_length=255, blank=True, verbose_name='ID сессии Stripe')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'Заказ №{self.id} - {self.total_price} USD'

    def calculate_total_price(self):
        total = 0
        for order_item in self.orderitem_set.all():
            total += order_item.item.price * order_item.quantity
        self.total_price = total
        self.save()
        return total

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.quantity} x {self.item.name} (заказ №{self.order.id})"

    def subtotal(self):
        return self.item.price * self.quantity

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
        # Чтобы товар не повторялся в заказе
        unique_together = ['order', 'item']



