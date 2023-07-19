from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': "Все отчёты", 'url_name': 'reports'},
        # {'title': "Архив", 'url_name': 'archive'},
        {'title': "О нас!", 'url_name': 'about'}]


def home(request):
    the_companies = TheCompany.objects.all()
    context = {'posts': the_companies,
               'menu': menu,
               'title': 'Главная страница'}
    return render(request, 'report/home.html', context=context)


def report(request):
    the_companies = TheCompany.objects.all()
    context = {'posts': the_companies,
               'menu': menu,
               'title': 'Отчёт'}
    return render(request, 'report/report.html', context=context)


def reports(request):
    the_companies = TheCompany.objects.all()
    context = {'posts': the_companies,
               'menu': menu,
               'title': 'Отчёты'}
    return render(request, 'report/reports.html', context=context)


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
    context = {'menu': menu,
               'title': 'О нас!'}
    return render(request, 'report/about.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Отчёт не найден</h1>')
