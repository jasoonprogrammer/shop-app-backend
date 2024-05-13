from django.contrib import admin
from .models import *
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(PriceUpdate)
admin.site.register(Transaction)
admin.site.register(Promo)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Category)
# Register your models here.