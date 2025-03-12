from django.shortcuts import render
from django.http import HttpResponse
def main_view(request):
    return render(request, 'main/index.html')  # Измените на index.html

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на django</h1>")

# Create your views here.
