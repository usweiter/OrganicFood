from celery import shared_task
from .models import Order
from django.core.mail import send_mail

@shared_task
def on_created_order(order_id):
	order = Order.objects.get(id=order_id)
	subject = "Order:{}".format(order.id)
	message = 'Dear {}\n\nOrder is successfully created. Order id:{}'.format(order.first_name, order.id)
	mail = send_mail(subject, message, 'OrganicFood@mail.ru', [order.email])

	return mail