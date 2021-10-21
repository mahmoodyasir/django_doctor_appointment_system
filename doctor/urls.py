from django.conf.urls import url
from django.urls import path
from . import views
from doctor import views as doctor_views

urlpatterns = [
    path("", views.general, name='home'),
    path("doctor-index/", views.index, name='doctor-home'),
    path("login-register/", views.login_register_page, name='login-register'),
    path("doctor-login/", views.doctor_login, name='doctor-login'),
    path("doctor-logout/", views.doctor_logout, name='doctor-logout'),
    path("doctor-info/<str:pk>/", views.doc_info, name='doctor-info'),
    path("doctor-update-info/<str:pk>/", views.doc_update_info, name='doctor-update-info'),
    path("doctor-final-update/<str:pk>/", views.doc_final_update, name='doctor-final-update'),
    path("doctor-appointment/<str:pk>/", views.doctor_appointment, name='doctor-appointment'),
    path("doctor-appointment-update/<str:pk>/", views.doctor_appointment_update, name='doctor-appointment-update'),
    path("doctor_appointment_form/<str:pk>/", views.doctor_appointment_form, name='doctor_appointment_form'),
    path("doctor_appointment_create/<str:pk>/", views.doctor_appointment_create, name='doctor_appointment_create'),
    path("doc_appointment_delete/<str:pk>/", views.doc_appointment_delete, name='doc_appointment_delete'),
    path("take_appointment/", views.take_appointment, name='take_appointment'),
    path("patient_appointment/<str:pk>/", views.patient_appointment, name='patient_appointment'),
    # url(r'^doctor/(?P<user_login_name>[\w\-]+)/$', doctor_views.doctor_appointment),
]

