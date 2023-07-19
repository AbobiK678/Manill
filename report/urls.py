from django.urls import path, include, re_path
from . import views
from .views import pageNotFound
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  # URLS Пути страниц
    path('', views.home, name='home'),  # !!!!!!!!!Поправить redirect!!!!!!!!!!!!!
    path('cats/<str:catid>', views.category, name='category'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name='archive'),
    path('report', views.report, name='report'),
    path('reports', views.reports, name='reports'),
    path('about', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
