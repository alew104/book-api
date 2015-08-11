from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(('GET',))
def root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
    })
