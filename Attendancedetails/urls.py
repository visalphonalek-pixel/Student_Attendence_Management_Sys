from django.urls import path
from . import views

urlpatterns = [
    
    path('attendances/', views.attendance_list, name='attendance_list'),
    path('attendances/create/', views.attendance_create, name='attendance_create'),
    path('attendances/<int:pk>/', views.attendance_detail, name='attendance_detail'),
    path('attendances/<int:pk>/edit/', views.attendance_edit, name='attendance_edit'),
    path('attendances/<int:pk>/delete/', views.attendance_delete, name='attendance_delete'),
]