from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Product, Category, File
from .serializers import CategorySerializer, FileSerializer, ProductSerializer


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={"request": request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, pk):
        subs = request.user.subscription_set.filter(expire_time__gt=timezone.now())
        if not subs.exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)


class FileListView(APIView):
    def get(self, request, product_id):
        files = File.objects.filter(pk=product_id)
        serializer = FileSerializer(files, many=True, context={"request": request})
        return Response(serializer.data)


class FileDetailView(APIView):
    def get(self, request, pk, product_id):
        try:
            file = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file, context={"request": request})
        return Response(serializer.data)


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={"request": request})
        return Response(serializer.data)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, context={"request": request})
        return Response(serializer.data)
