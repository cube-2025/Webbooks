from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render

def index(request):
    text_head = 'Книжный магазин'
    text_body = 'Это содержимое главной страницы сайта'
    context = {
        'text_head': text_head,
        'text_body': text_body
    }
    return render(request, 'catalog/index.html', context)
