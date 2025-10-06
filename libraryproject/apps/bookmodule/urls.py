from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books_home, name='books_home'),
    path('books/book-1/', views.book1, name='book1'),
    path('books/book-2/', views.book2, name='book2'),
    path('books/book-3/', views.book3, name='book3'),
]