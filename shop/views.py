from django.shortcuts import render
from shop.models import Product, Category

def shop(request):
	products = Product.objects.filter(available=True)
	return render(request, 'shop.html', {'products':products})