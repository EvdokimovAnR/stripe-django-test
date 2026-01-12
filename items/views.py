from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Order, OrderItem
from django.conf import settings
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return render(request, 'items/index.html')


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    context = {'item': item, 'stripe_public_key': settings.STRIPE_PUBLIC_KEY}
    return render(request, 'items/item_detail.html', context)


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                        'unit_amount': int(item.price * 100) # цена в центах
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f'http://{request.get_host()}/success',
            cancel_url=f'http://{request.get_host()}/cancel',
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def success(request):
    return render(request, 'items/success.html')


def cancel(request):
    return render(request, 'items/cancel.html')


def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})


def create_order(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('items')
        if not selected_items:
            return redirect('item_list')
        order = Order.objects.create()
        total_price = 0
        for item_id in selected_items:
            try:
                item = Item.objects.get(id=int(item_id))
                OrderItem.objects.create(
                    order=order,
                    item=item,
                    quantity = 1
                )
                total_price += item.price
            except Item.DoesNotExist:
                continue
        order.total_price = total_price
        order.save()
        return redirect('order_detail', order_id=order.id)
    items = Item.objects.all()
    return render(request, 'items/order_create.html', {'items': items})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order).select_related('item')
    context = {
        'order': order,
        'order_items': order_items,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'items/order_detail.html', context)


def buy_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    line_items = []

    for order_item in order_items:
        line_items.append({
            'price_data':{
                'currency': 'usd',
                'product_data': {
                    'name': order_item.item.name,
                },
                'unit_amount': int(order_item.item.price * 100)
            },
            'quantity': 1
        })
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = line_items,
            mode = 'payment',
            success_url=f'http://{request.get_host()}/success',
            cancel_url=f'http://{request.get_host()}/cancel',
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


