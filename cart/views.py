from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .cart import Cart
from shop.models import Product
from .forms import CartAddProductForm

def cart_add(request, id):

	cart = Cart(request)
	product = get_object_or_404(Product, id=id)

	if request.method == 'POST':
		form = CartAddProductForm(request.POST)

		if form.is_valid():
			form_cd = form.cleaned_data
			cart.add(product, quantity=form_cd['quantity'], update_quantity=form_cd['update'])

		return HttpResponse(200)
	
	else:
		cart.add(product)
		return HttpResponse(200)

def cart_remove(request, id):

	cart = Cart(request)
	cart.remove(id)

	return HttpResponse(200)

def cart_detail(request):
	cart = Cart(request)

	for item in cart:
		item['quantity_form'] = CartAddProductForm(
			initial={'quantity':item['quantity'], 'update':True})

	return render(request, 'cart_detail.html', {'cart':cart})
