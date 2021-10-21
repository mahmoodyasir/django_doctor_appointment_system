from django.contrib import admin
from .models import PatientInfo, BookAppointment

# Register your models here.


class PatientInfoAdmin(admin.ModelAdmin):
    search_fields = ['email', 'phone']
    list_filter = ['phone', 'name']
    list_display = ['id', 'user', 'name', 'email', 'phone']
    list_per_page = 10


class BookAppointmentAdmin(admin.ModelAdmin):
    search_fields = ['patient_id']
    list_filter = ['patient_id', 'payment']
    list_display = ['patient_id', 'appointment_id', 'doctor_id', 'doctor_name', 'serial', 'date_created', 'start_time',
                    'end_time', 'payment', 'checker']
    list_per_page = 10


admin.site.register(PatientInfo, PatientInfoAdmin)
admin.site.register(BookAppointment, BookAppointmentAdmin)
