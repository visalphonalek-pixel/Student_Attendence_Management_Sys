from django.shortcuts import render, redirect, get_object_or_404
from authentication.decorators import jwt_required
from .models import Student
from .forms import StudentForm

@jwt_required
def student_list(request):
    students = Student.objects.select_related('classroom').all()
    return render(request, "students/list.html", {"students": students})

@jwt_required
def student_create(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    return render(request, "students/form.html", {"form": form, "title": "Create Student"})

@jwt_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/detail.html", {"student": student})

@jwt_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    return render(request, "students/form.html", {"form": form, "title": "Edit Student"})

@jwt_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "students/confirm_delete.html", {"student": student})