from django.shortcuts import render
from authentication.decorators import jwt_required
from Students.models import Student
from Classrooms.models import ClassRoom
from Subjects.models import Subject
from Teachers.models import Teacher
from Attendances.models import Attendance

@jwt_required
def dashboard_view(request):
    context = {
        "total_students": Student.objects.count(),
        "total_classes": ClassRoom.objects.count(),
        "total_subjects": Subject.objects.count(),
        "total_teachers": Teacher.objects.count(),
        "total_attendances": Attendance.objects.count(),
    }
    return render(request, "dashboard/dashboard.html", context)