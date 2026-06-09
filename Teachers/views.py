from django.shortcuts import render, redirect, get_object_or_404
from authentication.decorators import jwt_required
from .models import Teacher
from .forms import TeacherForm

@jwt_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/list.html", {"teachers": teachers})

@jwt_required
def teacher_create(request):
    form = TeacherForm()
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    return render(request, "teachers/form.html", {"form": form, "title": "Create Teacher"})

@jwt_required
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, "teachers/detail.html", {"teacher": teacher})

@jwt_required
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(instance=teacher)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    return render(request, "teachers/form.html", {"form": form, "title": "Edit Teacher"})

@jwt_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect("teacher_list")
    return render(request, "teachers/confirm_delete.html", {"teacher": teacher})