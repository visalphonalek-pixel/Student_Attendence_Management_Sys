from django.urls import path
from . import views

urlpatterns = [
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("teachers/create/", views.teacher_create, name="teacher_create"),
    path("teachers/<int:pk>/", views.teacher_detail, name="teacher_detail"),
    path("teachers/<int:pk>/edit/", views.teacher_edit, name="teacher_edit"),
    path("teachers/<int:pk>/delete/", views.teacher_delete, name="teacher_delete"),
]