from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def lesson_4_page(request: HttpRequest) -> HttpResponse:
    context = {
        'page_name': 'Домашка по 4 занятию.',
        'text': 'Домашка по 4 занятию.'
    }

    return render(request, 'lesson_4.html', context)