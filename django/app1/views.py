from multiprocessing import context
from urllib import response
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

# import serializer
from books.serializers import BookSerializer

# import models
from .models import Book


class BooksView(APIView):
    serializer_class = BookSerializer
    def get(self, request):
        paginator = PageNumberPagination()
        queryset = Book.objects.all()
        context = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(context, many = True)
        return Response(paginator.get_paginated_response(serializer.data).data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def put(self, request, id):
        try:
            queryset = Book.objects.get(id=id)
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({' message' : 'Books record not exist'}, status=status.HTTP_404_NOT_FOUND)    
    def delete(self, request, id):
        try:
            queryset = Book.objects.get(id=id)
            queryset.delete()
            return Response({' message' : 'Books record deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({ 'message' : 'books record not exist'}, status=status.HTTP_404_NOT_FOUND)

class BookRecordView(APIView):
    serializer_Class = BookSerializer
    def get(self, request, id):
        try:
            queryset = Book.objects.get(id=id)
            serializer = self.serializer_Class(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({ "message" :  "book record not exist"}, status=status.HTTP_404_NOT_FOUND)
