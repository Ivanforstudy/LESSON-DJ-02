
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')  # Убедитесь, что используете правильный шаблон

def new(request):
    return render(request, 'main/new.html')
