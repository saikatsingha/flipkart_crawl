from rest_framework import serializers
from mobiles.models import Product_type, Product_details

class Product_type_Serializers (serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = ('id',
                  'product_name')

class Product_details_Serializers (serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = ('id', 
                  'company_name',
                  'price',
                  'photo',
                  'ram',
                  'internal_storage',
                  'expandable',
                  'display',
                  'camera',
                  'battery',
                  'processor',
                  'link',
                  'warranty',
                  'star',
                  'rating_review',
                  'in_the_box',
                  'product_type')