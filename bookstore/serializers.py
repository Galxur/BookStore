from django.utils.text import slugify
from rest_framework import serializers
from bookstore.models import Book , Category , Discount
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author','category','slug','price', 'in_stock', 'discount']
        def create(self, validated_data):
            book = Book(**validated_data)
            book.slug = slugify(book.title)
            book.save()
            return book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title','description']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['discount','description']