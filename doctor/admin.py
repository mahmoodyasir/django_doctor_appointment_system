from django.contrib import admin
from .models import DoctorInfo, DoctorSpec, Prescription, Appointment
# Register your models here.


class DoctorInfoAdmin(admin.ModelAdmin):
    search_fields = ['email', 'phone']
    list_filter = ['phone', 'name']
    list_display = ['id', 'user', 'name', 'email', 'phone']
    list_per_page = 10


class DoctorSpecAdmin(admin.ModelAdmin):
    search_fields = ['title', 'degree']
    list_filter = ['degree', 'institution']
    list_display = ['doctor_id', 'title', 'degree', 'institution', 'year_of_degree']
    list_per_page = 10


class PrescriptionAdmin(admin.ModelAdmin):
    search_fields = ['medicine']
    list_filter = ['medicine', 'usage_per_day']
    list_display = ['doctor_id', 'medicine', 'usage_per_day', 'total_duration']
    list_per_page = 10


class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['date_created']
    list_filter = ['start_time', 'end_time']
    list_display = ['id', 'doctor_id', 'date_created', 'start_time', 'end_time', 'total_patient', 'enrolled_patient']
    list_per_page = 10


admin.site.register(DoctorInfo, DoctorInfoAdmin)
admin.site.register(DoctorSpec, DoctorSpecAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Appointment, AppointmentAdmin)

