from django.urls import path
from . import views

urlpatterns = [
    path("classes/", views.classroom_list, name="classroom_list"),
    path("classes/create/", views.classroom_create, name="classroom_create"),
    path("classes/<int:pk>/", views.classroom_detail, name="classroom_detail"),
    path("classes/<int:pk>/edit/", views.classroom_edit, name="classroom_edit"),
    path("classes/<int:pk>/delete/", views.classroom_delete, name="classroom_delete"),
]