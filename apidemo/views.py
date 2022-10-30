from django.shortcuts import render
from .serializers import productserializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from data.models import products

# @api_view(["GET"])
# def firstview(request,*args,**kwargs):
    
#     data=products.objects.all()#.order_by("?").first()
#     data2=productserializer(data).data
#     #data['params']=request.GET
    
#     return Response(data2)

class firstview(generics.ListAPIView):
    queryset =products.objects.all()
    serializer_class=productserializer