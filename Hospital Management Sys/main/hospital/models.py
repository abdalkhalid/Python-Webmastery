from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        if self.pk is None or not User.objects.filter(pk=self.pk, password=self.password).exists():
            from django.contrib.auth.hashers import make_password
            self.password = make_password(self.password)
            self.is_active = True  
        super().save(*args, **kwargs)

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    medical_history = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Dr. {self.user.username} ({self.specialty})"

class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]
    shift = models.CharField(max_length=50, choices=SHIFT_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.get_shift_display()})"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"{self.patient} appointment with {self.doctor} on {self.date.strftime('%Y-%m-%d %H:%M')}"

def upload_to(instance, filename):
    return f'medical_records/patient_{instance.patient.id}/{filename}'

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"Medical record for {self.patient.name}"
