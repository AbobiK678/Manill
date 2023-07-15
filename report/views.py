from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = ["Главная", "Отчёты", "О нас!", "Обратная связь"]


def home(request):
    the_companies = TheCompany.objects.all()
    return render(request, 'report/home.html', {'posts': the_companies, 'menu': menu, 'title': 'Главная страница'})


def report(request):
    the_companies = TheCompany.objects.all()
    return render(request, 'report/report.html', {'posts': the_companies, 'menu': menu, 'title': 'Главная страница'})


def reports(request):
    the_companies = TheCompany.objects.all()
    return render(request, 'report/reports.html', {'posts': the_companies, 'menu': menu, 'title': 'Главная страница'})


def category(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Отчёт по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) < 2000:
        return redirect('home', permanent=True)  # перенаправление на главную страницу
    # handler500 = ошибка сервера
    # handler403 = доступ запрещен
    # handler400 = невозможно обработать запрос
    return HttpResponse(f'<h1>Отчёт за год </h1><p>{year}</p>')


def about(request):
    return render(request, 'report/about.html', {'menu': menu, 'title': 'О нас!'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Отчёт не найден</h1>')
