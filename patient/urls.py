from django.urls import path
from . import views

urlpatterns = [
    path("patient-index/", views.patient_index, name='patient-home'),
    path("patient-registration/", views.register_patient, name='patient-registration'),
    path("patient-info/<str:pk>/", views.patient_info, name='patient-info'),
    path("patient-update-info/<str:pk>/", views.patient_update_info, name='patient-update-info'),
    path("patient-final-update/<str:pk>/", views.patient_final_update, name='patient-final-update'),
    path("your_appointment/<str:pk>/", views.your_appointment, name='your_appointment'),
]
