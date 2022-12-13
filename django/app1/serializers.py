from dataclasses import fields
from rest_framework import serializers

# import models
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(required=True, min_length=3, max_length=20)
    author = serializers.CharField(required=True, min_length=3, max_length=30)
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author', 'published_year', 'language', 'cost', ]


