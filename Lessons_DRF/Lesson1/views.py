from django.shortcuts import render
from .models import Book
from rest_framework import status, generics

# Create your views here.

class BookList(generics.GenericAPIView):
    pass
