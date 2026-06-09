from django.db import models
from Attendances.models import Attendance
from Students.models import Student

class AttendanceDetail(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
        ('PE', 'Permission'),
    ]

    attendance = models.ForeignKey(
        Attendance,
        on_delete=models.CASCADE,   # delete session → delete all its details
        related_name='details'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        related_name='attendance_details'
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='P'
    )
    note = models.TextField(blank=True, null=True)

    class Meta:
        # One student appears only once per session
        unique_together = ['attendance', 'student']

    def __str__(self):
        return f"{self.student} — {self.get_status_display()}"