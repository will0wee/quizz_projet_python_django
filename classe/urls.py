from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.classroom),
    path('detail/<int:idClasse>', views.details_classroom),
]