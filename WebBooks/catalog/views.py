from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница магазин Книжный, что пишем, то и пишем')
