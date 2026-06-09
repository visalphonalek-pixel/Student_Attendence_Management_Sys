from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id', 'firstname', 'lastname',
            'gender', 'birthdate', 'phone', 'email',
            'address', 'classroom', 'status'
        ]
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }