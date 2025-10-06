from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book1/', views.book1, name='book1'),
    path('book2/', views.book2, name='book2'),
    path('book3/', views.book3, name='book3'),
]