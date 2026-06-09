from django import forms
from .models import Attendance, AttendanceDetail

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['classroom', 'subject', 'teacher', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }