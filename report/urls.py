from django.urls import path, include
from . import views
from .views import pageNotFound
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  # URLS Пути страниц
    path('', views.home),
    path('report', views.report),
    path('reports', views.reports),
    path('about', views.about)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
