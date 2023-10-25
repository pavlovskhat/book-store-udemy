from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg

from . models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")  # reverse order based on rating field
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()  # Generates default 404 pattern if one exists
    book = get_object_or_404(Book, slug=slug)  # Alternative to try except for 404 errors
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
