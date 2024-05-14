from rest_framework import serializers
from .models import *
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"

class PriceUpdateSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = PriceUpdate
        fields = "__all__"

    def get_timestamp(self, obj):
        return obj.timestamp.strftime("%B %d, %Y %I:%M:%S %p")

class SaleSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    promo = serializers.SerializerMethodField()
    class Meta:
        model = Sale
        fields = ['id', 'quantity', 'product', 'transaction', 'promo', 'price']

    def get_price(self, obj):
        transaction_date = obj.transaction.timestamp
        price = PriceUpdate.objects.filter(product = obj.product, timestamp__lte = obj.transaction.timestamp).order_by("-timestamp").first()
        return price.price
        
    def get_promo(self, obj):
        transaction_date = obj.transaction.timestamp
        promo = Promo.objects.filter(product = obj.product, startDate__lte = transaction_date, endDate__gte = transaction_date).first()
        if promo:
            serializer = PromoSerializer(promo)
            return serializer.data
        return None

class TransactionSerializer(serializers.ModelSerializer):
    sales = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'delivery_status', 'timestamp', 'sales']

    def get_sales(self, obj):
        sold = obj.get_sales()
        serializer = SaleSerializer(sold, many = True)
        return serializer.data
    
    
class PromoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promo
        fields = "__all__"