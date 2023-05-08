from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import TheCompany

menu = ["Главная", "Отчёты", "О нас!", "Обратная связь"]


def home(request):
    return render(request, 'report/home.html', {'menu': menu, 'title': 'Главная страница'})


def report(request):
    the_companies = TheCompany.objects.all()
    context = {'the_companies': the_companies}
    return render(request, 'report/report.html', context)


#def category(request, catid):
#    if request.POST:
#        print(request.POST)


def reports(request):
    the_companies = TheCompany.objects.all()
    context = {'the_companies': the_companies}
    return render(request, 'report/reports.html', context)


def about(request):
    return render(request, 'report/about.html', {'menu': menu, 'title': 'О нас!'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Отчёт не найден</h2>')