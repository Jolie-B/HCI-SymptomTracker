from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('callendar/', views.callendar, name='callendar'),
    path('stats/', views.stats, name='stats'),
    path('<slug:day_slug>', views.date, name='day')
]