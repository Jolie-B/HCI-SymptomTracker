from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stats/', views.stats, name='stats'),
    path('statsload', views.statsload, name='statsload'),
    path('<slug:day_slug>', views.date, name='day')

]