from django.http import HttpResponse
# импортируем функцию render
from django.shortcuts import render

def first_page(request):
    a = '<h1>Hello World</h1>'
    return render(request, './index.html')