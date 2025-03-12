from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ссылка на функцию index
    path('new/', views.new, name='new'),   # Ссылка на функцию new
]
