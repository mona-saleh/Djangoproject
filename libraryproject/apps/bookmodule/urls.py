from django.urls import path
from . import views

urlpatterns = [
    path('html5/links', views.links_page),
    path('html5/text/formatting', views.formatting_page),
    path('html5/listing', views.listing_page),
    path('html5/tables', views.tables_page),
    path('books/search', views.search_books, name='search_books'),
    path('books/search', views.search_books, name='search_books'),
    path('books/simple/query', views.simple_query, name='simple-query'),
    path('books/complex/query', views.complex_query, name='complex-query'),
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='lab8_task7'),
    path('', views.home, name='home'),
]