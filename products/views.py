from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Category, File
from .serializers import CategorySerializer, FileSerializer, ProductSerializer

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

