from django.forms import ModelForm
from .models import *


class UpdateForm(ModelForm):
    class Meta:
        model = DoctorInfo
        fields = ['name', 'email', 'phone', 'age', 'address']


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_created', 'start_time', 'end_time', 'total_patient']


class CreateAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

