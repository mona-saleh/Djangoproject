from django.shortcuts import render

def links_page(request):
    return render(request, 'books/html5/links.html')

def formatting_page(request):
    return render(request, 'books/html5/formatting.html')

def listing_page(request):
    return render(request, 'books/html5/listing.html')

def tables_page(request):
    return render(request, 'books/html5/tables.html')

def getBooksList():
    book1 = {'id': 1234321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 6549876, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 44221134, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]


def search_books(request):
    books = getBooksList()
    newBooks = []

    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        for b in books:
            match = False
            if isTitle and keyword in b['title'].lower():
                match = True
            if isAuthor and keyword in b['author'].lower():
                match = True
            if match:
                newBooks.append(b)

        return render(request, 'books/bookList.html', {'books': newBooks})

    return render(request, 'books/search.html')