from django.urls import path
from .views import register_hospital, success_page, register_doctor, doctor_success, register_patient,patient_success
from .views import register_intern, intern_success
urlpatterns = [
    path('register/', register_hospital, name="register_hospital"),
    path('success/', success_page, name="success"),
    path('register/doctor/', register_doctor, name="register_doctor"),
    path('doctor/success/', doctor_success, name="doctor_success"),
    path('register/patient/', register_patient, name="register_patient"),
    path('patient/success/', patient_success, name="patient_success"),
    path('register/intern/', register_intern, name="register_intern"),
    path('intern/success/', intern_success, name="intern_success"),
]
