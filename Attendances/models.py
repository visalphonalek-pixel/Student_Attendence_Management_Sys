from django.db import models
from Classrooms.models import ClassRoom
from Subjects.models import Subject
from Teachers.models import Teacher

class Attendance(models.Model):
    # One session = one class, one subject, one teacher, one date
    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.PROTECT,
        related_name='attendances'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='attendances'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        related_name='attendances'
    )

    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Can't have two sessions for same class+subject on same day
        unique_together = ['classroom', 'subject', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.classroom} | {self.subject} | {self.date}"