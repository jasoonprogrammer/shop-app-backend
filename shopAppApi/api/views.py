from django.shortcuts import render
from django.core.files import File
from .serializers import *
# Create your views here.
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
import json
import requests
import time
category = Category.objects.first()
# with open("case_data.json", "r") as f:
#     data = json.load(f)
    
# for d in data:
#     r = requests.get(d['image'])
#     with open("test.jpg", "wb") as f:
#         f.write(r.content)
#     pr = Product.objects.create(name = d['title'], price = d['price'], image = File(open("test.jpg", "rb")), category = category)

class CategoryCreateAPI(CreateAPIView):
    serializer_class = CategorySerializer

class CategoryListAPI(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryUpdateAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

#---------------------------------------

class ProductListAPI(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductCreateAPI(CreateAPIView):
    serializer_class = ProductSerializer

class ProductUpdateAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class PriceUpdateCreateAPI(CreateAPIView):
    serializer_class = PriceUpdateSerializer

class PriceUpdateListAPI(ListAPIView):
    serializer_class = PriceUpdateSerializer
    queryset = PriceUpdate.objects.all()

class PriceUpdateAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = PriceUpdateSerializer
    queryset = PriceUpdate.objects.all()


class SaleListAPI(ListAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

class SaleCreateAPI(CreateAPIView):
    serializer_class = SaleSerializer

class SaleUpdateAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

class TransactionCreateAPI(CreateAPIView):
    serializer_class = TransactionSerializer

class TransactionRetrieveAPI(RetrieveAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

class TransactionListAPI(ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()