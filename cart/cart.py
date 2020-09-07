from django.conf import settings
from shop.models import Product
from decimal import Decimal

class Cart:
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def __iter__(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids) #ВОЗМОЖНА ОШИБКА

		cart = self.cart.copy() #cart = {0:{...}, 1:{...}, 2:{'price': ,'quantity': ,}}
		
		for product in products:
			cart[str(product.id)]['product'] = product #{2:{'price', 'quantity', 'product'}}
		for item in cart.values():
			item['total_price'] = item['quantity'] * Decimal(item['price'])#{2:{'price', 'quantity', 'product', 'total_price'}}
			yield item

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def save(self):
		self.session.modified = True

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.save()

	def add(self, product, quantity=1, update_quantity=False):
		product_id = str(product.id)

		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

	def remove(self, product_id):
		product_id = str(product_id)

		if product_id in self.cart:
			del self.cart[product_id]
		self.save()
		'''else:
			return error_404()'''
