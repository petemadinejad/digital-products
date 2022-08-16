from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Category, File
from .serializers import CategorySerializer, FileSerializer, ProductSerializer


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={"request": request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)
