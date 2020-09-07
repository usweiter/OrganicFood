from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
	path('remove/<int:id>', views.cart_remove, name='cart_remove'),
	path('add/<int:id>', views.cart_add, name='cart_add'),
	path('', views.cart_detail, name='cart_detail')
]