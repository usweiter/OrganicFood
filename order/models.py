from django.db import models
from shop.models import Product

class Order(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	city = models.CharField(max_length=100)
	street = models.CharField(max_length=100)
	postal_code = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order: {}'.format(self.id)

	def get_total_price(self):
		return sum(product.total_price() for product in self.products.all())

class OrderProduct(models.Model):
	product = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE)
	order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def total_price(self):
		return self.quantity * self.price

