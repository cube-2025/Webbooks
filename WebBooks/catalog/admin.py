from django.contrib import admin
from .models import Author, BookInstance, Book, Genre, Status, Language, Publisher

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Status)
admin.site.register(Language)
admin.site.register(Publisher)

