from django.db import models
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from mobiles.models import Product_details, Product_type
from mobiles.serializers import Product_type_Serializers, Product_details_Serializers

# Create your views here.

@csrf_exempt

def mobilesAPI(request, id=0):
    if request.method == 'GET':
        mobiles = Product_details.objects.all()
        mobiles_serializer = Product_type_Serializers.data(mobiles, many=True)
        return JsonResponse(mobiles_serializer.data, safe=False)