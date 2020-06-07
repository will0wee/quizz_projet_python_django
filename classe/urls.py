from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.classroom, name="listeClassRoom"),
    path('<classroomId>', views.classroom, name="listeClassRoom"),
    path('detail/<int:classroomId>', views.details_classroom, name="detailClassRoom"),
    path('delete/<int:classroomId>', views.delete_classroom, name="deleteClassRoom"),
    path('delete/eleve/<int:classroomId>/<int:eleveId>', views.delete_student, name="deleteStudent"),
]