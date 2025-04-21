from django.urls import path
from .views import Book
urlpatterns = [
    path('books', Book.as_view(), name='book'),
]