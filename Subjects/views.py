from django.shortcuts import render, redirect, get_object_or_404
from authentication.decorators import jwt_required
from .models import Subject
from .forms import SubjectForm

@jwt_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, "subjects/list.html", {"subjects": subjects})

@jwt_required
def subject_create(request):
    form = SubjectForm()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subject_list")
    return render(request, "subjects/form.html", {"form": form, "title": "Create Subject"})

@jwt_required
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, "subjects/detail.html", {"subject": subject})

@jwt_required
def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(instance=subject)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect("subject_list")
    return render(request, "subjects/form.html", {"form": form, "title": "Edit Subject"})

@jwt_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        subject.delete()
        return redirect("subject_list")
    return render(request, "subjects/confirm_delete.html", {"subject": subject})