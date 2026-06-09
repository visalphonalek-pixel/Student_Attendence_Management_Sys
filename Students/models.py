from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    # Add any other classroom fields you need

    def __str__(self):
        return self.name

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),
        ('Dropped', 'Dropped'),
        ('Graduated', 'Graduated'),
    ]

    student_id  = models.CharField(max_length=20, unique=True, verbose_name='Student ID')
    firstname   = models.CharField(max_length=100)
    lastname    = models.CharField(max_length=100)
    email       = models.EmailField(unique=True, blank=True, null=True)
    phone       = models.CharField(max_length=20, blank=True)
    gender      = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    birthdate   = models.DateField(null=True, blank=True)
    address     = models.TextField(blank=True)
    classroom   = models.ForeignKey(
                    ClassRoom,
                    on_delete=models.SET_NULL,
                    null=True, blank=True,
                    related_name='students'
                  )
    status      = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Enrolled')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return f"{self.student_id} – {self.firstname} {self.lastname}"

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"