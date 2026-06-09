from django.shortcuts import render, redirect, get_object_or_404
from authentication.decorators import jwt_required
from .models import ClassRoom
from .forms import ClassRoomForm

@jwt_required
def classroom_list(request):
    classrooms = ClassRoom.objects.all()
    return render(request, "classrooms/list.html", {"classrooms": classrooms})

@jwt_required
def classroom_create(request):
    form = ClassRoomForm()
    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("classroom_list")
    return render(request, "classrooms/form.html", {"form": form, "title": "Create Classroom"})

@jwt_required
def classroom_detail(request, pk):
    classroom = get_object_or_404(ClassRoom, pk=pk)
    return render(request, "classrooms/detail.html", {"classroom": classroom})

@jwt_required
def classroom_edit(request, pk):
    classroom = get_object_or_404(ClassRoom, pk=pk)
    form = ClassRoomForm(instance=classroom)
    if request.method == "POST":
        form = ClassRoomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect("classroom_list")
    return render(request, "classrooms/form.html", {"form": form, "title": "Edit Classroom"})

@jwt_required
def classroom_delete(request, pk):
    classroom = get_object_or_404(ClassRoom, pk=pk)
    if request.method == "POST":
        classroom.delete()
        return redirect("classroom_list")
    return render(request, "classrooms/confirm_delete.html", {"classroom": classroom})