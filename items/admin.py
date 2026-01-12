from django.contrib import admin
from .models import Item, OrderItem, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')


class OrderItemInline(admin.TabularInline):
    """Встроенное редактирование товаров в заказе"""
    model = OrderItem
    extra = 1  # Количество пустых строк для добавления
    raw_id_fields = ['item']  # Поле поиска вместо выпадающего списка


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'paid', 'created_at')
    list_filter = ('paid', 'created_at')
    search_fields = ('id', 'stripe_session_id')
    inlines = [OrderItemInline]  # Добавляем inline для OrderItem


