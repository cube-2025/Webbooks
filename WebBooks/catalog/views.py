from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance
from django.views.generic import ListView, DetailView

from django.shortcuts import render

def index(request):
    text_head = 'Книжный магазин'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact = 2).count()
    author = Author.objects
    num_authors = Author.objects.count()
    context = {
        'text_head': text_head,
        'books': books, 'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'author': author, 'num_authors':num_authors
    }
    return render(request, 'catalog/index.html', context)

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class AuthorListView(ListView):
    model = Author
class AuthorDetailView(DetailView):
    model = Author