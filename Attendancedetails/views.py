from django.shortcuts import render, redirect, get_object_or_404
from authentication.decorators import jwt_required
from .models import AttendanceDetail
from .forms import AttendanceDetailForm

@jwt_required
def attendance_detail_list(request):
    details = AttendanceDetail.objects.select_related(
        'attendance', 'student', 'attendance__classroom'
    ).all()
    return render(request, 'attendancedetails/list.html', {'details': details})

@jwt_required
def attendance_detail_create(request):
    initial = {}
    attendance_id = request.GET.get('attendance')
    if attendance_id:
        try:
            initial['attendance'] = int(attendance_id)
        except ValueError:
            pass
    form = AttendanceDetailForm(request.POST or None, initial=initial)
    if form.is_valid():
        detail = form.save()
        if attendance_id:
            return redirect('attendance_detail', pk=detail.attendance.pk)
        return redirect('attendance_detail_list')
    return render(request, 'attendancedetails/form.html', {'form': form, 'title': 'Mark Attendance'})

@jwt_required
def attendance_detail_detail(request, pk):
    detail = get_object_or_404(
        AttendanceDetail.objects.select_related(
            'attendance', 'student', 'attendance__classroom', 'attendance__subject'
        ),
        pk=pk
    )
    return render(request, 'attendancedetails/detail.html', {'detail': detail})

@jwt_required
def attendance_detail_edit(request, pk):
    detail = get_object_or_404(AttendanceDetail, pk=pk)
    form = AttendanceDetailForm(request.POST or None, instance=detail)
    if form.is_valid():
        detail = form.save()
        return redirect('attendance_detail', pk=detail.attendance.pk)
    return render(request, 'attendancedetails/form.html', {'form': form, 'title': 'Edit Attendance Record'})

@jwt_required
def attendance_detail_delete(request, pk):
    detail = get_object_or_404(AttendanceDetail, pk=pk)
    attendance_pk = detail.attendance.pk
    if request.method == 'POST':
        detail.delete()
        return redirect('attendance_detail', pk=attendance_pk)
    return render(request, 'attendancedetails/confirm_delete.html', {'detail': detail})