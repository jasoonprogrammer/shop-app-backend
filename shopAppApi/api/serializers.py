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

    class Meta:
        model = PriceUpdate
        fields = "__all__"

class SaleSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    class Meta:
        model = Sale
        fields = ['id', 'quantity', 'product', 'transaction', 'price']

    def get_price(self, obj):
        price = PriceUpdate.objects.filter(product = obj.product, timestamp__lte = obj.transaction.timestamp).first().price
        return price
        # print(obj)
        # return obj.get_price()

class TransactionSerializer(serializers.ModelSerializer):
    sales = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ['id', 'delivery_status', 'timestamp', 'sales']

    def get_sales(self, obj):
        sold = obj.get_sales()
        serializer = SaleSerializer(sold, many = True)
        return serializer.data
    
