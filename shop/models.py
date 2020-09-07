from django.db import models
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	
	class Meta:
		ordering = ("name", )
		verbose_name = "category"
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name
	'''def get_absolute_url(self):
		return reverse('shop:catalog_by_category', args=[self.slug])'''

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = "products")
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	volume = models.PositiveSmallIntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(default="static/default.jpg", upload_to="products/%Y/%m/%d")
	available = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=("category", )

	def __str__(self):
		return self.name

	'''def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id])'''