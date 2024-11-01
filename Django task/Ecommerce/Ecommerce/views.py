from django.shortcuts import render
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    orders_with_total = [{'order': order, 'total_price': order.total_price()} for order in orders]

    return render(request, 'order_list.html', {'orders_with_total': orders_with_total})
