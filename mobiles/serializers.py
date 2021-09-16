from rest_framework import serializers
from mobiles.models import Product_type, Product_details

class Product_type_Serializers (serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = ('id', 
                  'product_name')