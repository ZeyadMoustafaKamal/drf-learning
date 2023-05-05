from rest_framework import serializers
from .models import Product

class ProductSerialzer(serializers.ModelSerializer):

    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = 'id','price','name','content','discount'

    def get_discount(self,obj):
        return obj.sale_price

