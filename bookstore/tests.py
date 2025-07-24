from django.test import TestCase

# Create your tests here.





from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from bookstore.serializers import BookSerializer, CategorySerializer, DiscountSerializer
from .models import Book , Category , Discount
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['title','author','category','in_stock', 'price']
    filter_class = BookFilter #?
    search_fields = ['title','author','category']
    filterset_fields = ['in_stock']
    #If all you need is simple equality-based filtering, you can set a filterset_fields attribute on the view, or
    # viewset, listing the set of fields you wish to filter against.
    def get_queryset(self):
        queryset = Book.objects.all()
        category_id_parameters = self.request.query_params.get('category_id')
        if category_id_parameters is not None:
            queryset = queryset.filter(category__id=category_id_parameters)
        return queryset

    def get_serializer_context(self):
        return {'request': self.request}

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get_serializer_context(self):
        return {'request': self.request}

class DiscountViewSet(ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    def get_serializer_context(self):
        return {'request': self.request}