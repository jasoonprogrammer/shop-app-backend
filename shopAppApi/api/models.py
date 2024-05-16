from typing import Collection
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from django_resized import ResizedImageField
import datetime
# Create your models here.
def random_sku() -> str:
    while True:
        sku = get_random_string(length = 15)
        if Product.objects.filter(sku = sku).exists():
            pass
        else:
            break
    return sku
def phoneValidator(value):
    if not value.startswith("09"):
        raise ValidationError("Number should star with 09")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    firstName = models.CharField(max_length = 100)
    middleName = models.CharField(max_length = 100, null = True, blank = True)
    lastName = models.CharField(max_length = 100)
    birthdate = models.DateField()
    isSeller = models.BooleanField(default = False)
    dateRegistered = models.DateField(default = datetime.datetime.now)
    phoneNumber = models.CharField(max_length = 11, validators = [phoneValidator])
    emailAddress = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length = 50)

class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    sku = models.CharField(max_length = 50, unique = True, default = random_sku)
    price = models.FloatField()
    stock = models.IntegerField(default = 0)
    image = ResizedImageField(size = [200, 200], upload_to = "product_images", default = "image1.jpg")
    #foreign field so we can add more than 1 product can use the same category
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        #works as a signal, but can detect price change and create new PriceUpdate object
        old = type(self).objects.get(pk = self.pk) if self.pk else None
        super(Product, self).save(*args, **kwargs)
        if old and old.price != self.price:
            PriceUpdate.objects.create(product = self, price = self.price, timestamp = datetime.datetime.now())
        elif not old:
            PriceUpdate.objects.create(product = self, price = self.price, timestamp = datetime.datetime.now())

    def __str__(self):
        return f"{self.name} - {self.id}"

class PriceUpdate(models.Model):
    # to track the prices, so we dont need to add a price row to other tables that causes redundancy.
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    price = models.FloatField()
    timestamp = models.DateTimeField(default = datetime.datetime.now)

    def __str__(self):
        return f"{self.price} - {self.timestamp.strftime("%b %d, %Y %I:%M:%S %p")} - {self.product.name} - {self.product.id}"


class Tag(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)

class Transaction(models.Model):
    ACCEPTED = "ACCEPTED"
    RECEIVED = "RECEIVED"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    CANCELLED = "CANCELLED"
    DELIVERY_STATUS_CHOICES = {
        ACCEPTED: "Accepted",
        RECEIVED : "Received",
        IN_TRANSIT : "In Transit",
        OUT_FOR_DELIVERY : "Out for Delivery",
        CANCELLED : "Cancelled"
    }
    
    def get_sales(self):
        return Sale.objects.filter(transaction = self)
    
    @property
    def total(self):
        sales = self.get_sales()
        sale_total = sum([x.total for x in sales])
        return sale_total

    timestamp = models.DateTimeField(default = datetime.datetime.now)
    delivery_status = models.CharField(max_length = 20, choices = DELIVERY_STATUS_CHOICES, default = ACCEPTED)

    def __str__(self):
        return f"{self.id} - {self.delivery_status} - {self.timestamp.strftime("%b %d, %Y %I:%M:%S %p")}"

class Sale(models.Model):
    
    @property
    def total(self):
        return self.get_price() * self.product
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    #foreign key because 1 transaction can have multiple products sold.
    transaction = models.ForeignKey(Transaction, on_delete = models.CASCADE)

class ProductAd(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    viewCount = models.IntegerField(default = 0)
    maxViewCount = models.IntegerField()

    @property
    def remainingCount(self):
        return self.maxViewCount - self.viewCount

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    added = models.DateTimeField(default = datetime.datetime.now)

class Promo(models.Model):
    name = models.TextField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    discount = models.FloatField()

    def full_clean(self, exclude: Collection[str] | None = ..., validate_unique: bool = ..., validate_constraints: bool = ...) -> None:
        if self.startDate > self.endDate:
            raise ValidationError("Can't end before starting")
        else:
            promos = Promo.objects.filter(product = self.product)
            #check for promo overlapping
            for promo in promos:
                d1 = self
                d2 = promo
                if (d1.startDate < d2.startDate < d1.endDate or d2.startDate < d1.startDate < d2.endDate 
                    and 
                d1.startDate > d2.endDate > d1.endDate or d2.startDate > d1.endDate > d2.endDate):
                    raise ValidationError("Promos can't overlap")
        return super().full_clean(exclude, validate_unique, validate_constraints)

    def __str__(self):
        return f'{self.name} on {self.product.name[:20]}... : {self.startDate.strftime("%b %d, %Y %I:%M:%S %p")} - {self.endDate.strftime("%b %d, %Y %I:%M:%S %p")}'