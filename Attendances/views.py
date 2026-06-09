from django.shortcuts import render, redirect, get_object_or_404
from authentication.decorators import jwt_required
from .models import Attendance
from .forms import AttendanceForm

@jwt_required
def attendance_list(request):
    attendances = Attendance.objects.select_related('classroom', 'subject', 'teacher').all()
    return render(request, 'attendances/list.html', {'attendances': attendances})

@jwt_required
def attendance_create(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('attendance_list')
    return render(request, 'attendances/form.html', {'form': form, 'title': 'Create Attendance Session'})

@jwt_required
def attendance_detail(request, pk):
    attendance = get_object_or_404(
        Attendance.objects.select_related('classroom', 'subject', 'teacher'),
        pk=pk
    )
    details = attendance.details.select_related('student').all()
    return render(request, 'attendances/detail.html', {
        'attendance': attendance,
        'details': details
    })

@jwt_required
def attendance_edit(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    form = AttendanceForm(request.POST or None, instance=attendance)
    if form.is_valid():
        form.save()
        return redirect('attendance_list')
    return render(request, 'attendances/form.html', {'form': form, 'title': 'Edit Attendance Session'})

@jwt_required
def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'attendances/confirm_delete.html', {'attendance': attendance})