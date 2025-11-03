from django.shortcuts import render
from .models import Book
from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Student, Address
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

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='and')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookList.html', {'books': mybooks})
    else:
        return render(request, 'index.html')
    
    # Task 1: كتب سعرها <= 80 باستخدام Q
def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'books/lab8_task1.html', {'books': books})

# Task 2: edition > 3 و (العنوان أو المؤلف يحتوي "co")
def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'books/lab8_task2.html', {'books': books})

# Task 3: عكس 2 باستخدام ~
def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & (~Q(title__icontains='co') | ~Q(author__icontains='co'))
    )
    return render(request, 'books/lab8_task3.html', {'books': books})

# Task 4: ترتيب حسب العنوان
def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books/lab8_task4.html', {'books': books})

# Task 5: تجميع (عدد/مجموع/متوسط/أعلى/أدنى سعر)
def lab8_task5(request):
    metrics = Book.objects.aggregate(
        books_count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'books/lab8_task5.html', {'metrics': metrics})

# Task 7: عدد الطلاب في كل مدينة
def lab8_task7(request):
    data = (
        Student.objects
        .values('address__city')
        .annotate(count=Count('id'))
        .order_by('address__city')
    )
    return render(request, 'books/lab8_task7.html', {'data': data})

def home(request):
    return render(request, 'books/home.html')