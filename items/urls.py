from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
    path('buy-order/<int:order_id>/', views.buy_order, name='buy_order'),
    path('item_list/', views.item_list, name='item_list'),
    path('create_order/', views.create_order, name='create_order'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]