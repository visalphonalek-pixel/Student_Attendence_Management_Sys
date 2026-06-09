from django import forms
from .models import  AttendanceDetail

class AttendanceDetailForm(forms.ModelForm):
    class Meta:
        model = AttendanceDetail
        fields = ['attendance', 'student', 'status', 'note']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 2}),
        }