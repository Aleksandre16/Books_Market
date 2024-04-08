from django.http import JsonResponse
from django.shortcuts import render

from market.models import Book


def get_books(request):
    books = Book.objects.all()
    return JsonResponse({'books': list(books.values())})


def get_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        return JsonResponse({'book': {
            'name': book.name,
            'author': book.author,
            'price': book.price,
            'page_count': book.page_count,
            'category': book.category,
            'image': book.image.url if book.image else None, }})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
