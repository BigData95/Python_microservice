
#Utils
import random

#Django
from django.http import Http404
from django.shortcuts import render
# Rest framework
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

#Models
from .models import Product, User
from .producer import publish
#Serializers
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
    
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class  UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        try:
            user = random.choice(users)
        except Exception:
            user = User.objects.create()

        return Response({
            'id': user.id
        })
