from django.shortcuts import render

def book_list(request):
    return render(request, 'books/index.html')

def book1(request):
    return render(request, 'books/book-1.html')

def book2(request):
    return render(request, 'books/book-2.html')

def book3(request):
    return render(request, 'books/book-3.html')