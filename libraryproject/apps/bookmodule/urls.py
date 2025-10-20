from django.urls import path
from . import views

urlpatterns = [
    path('html5/links', views.links_page),
    path('html5/text/formatting', views.formatting_page),
    path('html5/listing', views.listing_page),
    path('html5/tables', views.tables_page),
    path('books/search', views.search_books, name='search_books'),
    path('books/search', views.search_books, name='search_books'),
]