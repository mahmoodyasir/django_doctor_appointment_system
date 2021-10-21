from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DoctorInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name


class DoctorSpec(models.Model):
    doctor_id = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=150, null=False, blank=False)
    institution = models.CharField(max_length=150, null=False, blank=False)
    year_of_degree = models.DateField()

    def __str__(self):
        return self.title


class Prescription(models.Model):
    doctor_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    medicine = models.CharField(max_length=150, null=False, blank=False)
    usage_per_day = models.TextField(null=False)
    total_duration = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.medicine


class Appointment(models.Model):
    doctor_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_patient = models.IntegerField(null=False, blank=False)
    enrolled_patient = models.IntegerField(null=False, blank=False, default=0)

    def __int__(self):
        return self.total_patient


