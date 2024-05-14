from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import *

# @receiver(post_save , sender = Product)
# def instantiatePrice(sender , instance , created , **kwargs):
#     # instance is the object of the User model which has just been created and it fired this signal .
#     if created:
#         PriceUpdate.objects.create(product = instance, price = instance.price)


# @receiver(post_save , sender = Sale)
# def setUserPassowrd(sender , instance , created , **kwargs):
#     # instance is the object of the User model which has just been created and it fired this signal .
#     if created:
#         product = instance.product
#         product.quantity = instance.quantity
#         product.save()