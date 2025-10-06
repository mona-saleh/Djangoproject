from django.shortcuts import render

def user_list(request):
    users = [
        {'name': 'Mona Saleh', 'email': 'mona@example.com'},
        {'name': 'Sara Ali', 'email': 'sara@example.com'},
        {'name': 'Omar Nasser', 'email': 'omar@example.com'},
    ]
    return render(request, 'user_list.html', {'users': users})