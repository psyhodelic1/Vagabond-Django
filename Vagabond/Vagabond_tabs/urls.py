from django.urls import path

from . import views

app_name = 'Vagabond_tabs'
urlpatterns = [
    path('', views.IndexView, name="index"),
    path('header/', views.HeaderView, name="header"),
]
