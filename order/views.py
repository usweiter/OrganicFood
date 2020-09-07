from django.shortcuts import render
from .models import Order, OrderProduct
from .forms import OrderForm
from cart.cart import Cart

def create_order(request):
	order_form = OrderForm()
	cart = Cart(request)
	if request.method == 'POST':
		order_form = OrderForm(request.POST)
		if order_form.is_valid():
			order = order_form.save()
			for item in cart:
				OrderProduct.objects.create(
						order=order,
						product=item['product'],
						quantity=item['quantity'],
						price=item['price']
					)
			cart.clear()
			return render(request, 'created_order.html', {'order':order})
	return render(request, 'create_order.html', {'order_form':order_form, 'cart':cart})
	