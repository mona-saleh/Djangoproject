from django.contrib import admin
from .models import Book
from .models import Publisher, Author, BookLab9
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(BookLab9)