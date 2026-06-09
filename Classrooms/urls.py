from django.urls import path
from . import views

urlpatterns = [
    path("classrooms/", views.classroom_list, name="classroom_list"),
    path("classrooms/create/", views.classroom_create, name="classroom_create"),
    path("classrooms/<int:pk>/", views.classroom_detail, name="classroom_detail"),
    path("classrooms/<int:pk>/edit/", views.classroom_edit, name="classroom_edit"),
    path("classrooms/<int:pk>/delete/", views.classroom_delete, name="classroom_delete"),
]