from django.db import models
from django.contrib.auth.models import User
from doctor.models import DoctorInfo

# Create your models here.


class PatientInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name


class BookAppointment(models.Model):
    patient_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    appointment_id = models.CharField(max_length=50, null=True, blank=True)
    doctor_id = models.CharField(max_length=50, null=True, blank=True)
    doctor_name = models.CharField(max_length=100, null=True, blank=True)
    serial = models.IntegerField(null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    payment = models.BooleanField(null=False, blank=False, default=False)
    checker = models.IntegerField(null=False, blank=False, default=0)

    def __bool__(self):
        return self.payment



