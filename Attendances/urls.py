from django.urls import path
from . import views

urlpatterns = [
    path('attendance-details/', views.attendance_detail_list, name='attendance_detail_list'),
    path('attendance-details/create/', views.attendance_detail_create, name='attendance_detail_create'),
    path('attendance-details/<int:pk>/', views.attendance_detail_detail, name='attendance_detail_detail'),
    path('attendance-details/<int:pk>/edit/', views.attendance_detail_edit, name='attendance_detail_edit'),
    path('attendance-details/<int:pk>/delete/', views.attendance_detail_delete, name='attendance_detail_delete'),
]