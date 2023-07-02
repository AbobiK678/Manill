from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import TheCompany

menu = ["Главная", "Отчёты", "Категории", "О нас!", "Обратная связь"]


def home(request):  # Домашня страница
    return render(request, 'report/home.html', {'menu': menu, 'title': 'Главная страница'})


def report(request):  # Страница отчёта
    the_companies = TheCompany.objects.all()
    context = {'the_companies': the_companies}
    return render(request, 'report/report.html', context)


def cats(request, cat):  # Страница категорий
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Отчёты по категориям</h1><p>{cat}</p>")


def reports(request):  # Страница отчётов
    the_companies = TheCompany.objects.all()
    context = {'the_companies': the_companies}
    return render(request, 'report/reports.html', context)


def about(request):  # Страница "О нас!"
    return render(request, 'report/about.html', {'menu': menu, 'title': 'О нас!'})


def pageNotFound(request, exception):  # Страница ошибки "Страница не найдена"
    return HttpResponseNotFound('<h1>Отчёт не найден</h1>')
