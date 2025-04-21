from .models import Book
from rest_framework import status, generics
from .serializers import BookSerializer


# Create your views here.

class BookList(generics.ListCreateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
         
