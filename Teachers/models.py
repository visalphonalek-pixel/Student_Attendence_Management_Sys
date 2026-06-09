from django.db import models
from django.contrib.auth.models import User
from Subjects.models import Subject  # ← import from Subjects app

class Teacher(models.Model):
    # Links this Teacher profile to a Django login account
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='teacher_profile'
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # A teacher can teach many subjects
    subjects = models.ManyToManyField(
        Subject,
        blank=True,
        related_name='teachers'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"