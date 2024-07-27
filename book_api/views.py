from rest_framework.views import APIView
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookView(APIView):
    def get_book_by_PK(self, pk):
        try:
            book = Book.objects.get(pk=pk)
            return book
        except:
            return Response({
                'error': 'Book not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = self.get_book_by_PK(pk)
        if isinstance(book, Response):
            return book
        
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put (self, request, pk):
        book = self.get_book_by_PK(pk)
        if isinstance(book, Response):
            return book
        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_book_by_PK(pk)
        if isinstance(book, Response):
            return book
        
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.http import JsonResponse
# from book_api.models import Book
# from book_api.serializer import BookSerializer

# Create your views here.
# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all() # It returns something called Complex Data
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)
    
"""
    This is another way to do it
    booksPython = list(books.values()) Python Data Structure
    return JsonResponse({
        'books': booksPython
    })
"""

# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else: 
#         return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk): 
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Book not found'
#         }, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)