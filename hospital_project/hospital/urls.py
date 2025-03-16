from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

# Importing views
from .views import (
    index, register_hospital, register_doctor, doctor_dashboard,
    register_patient, patient_success, doctor_login, register_intern, intern_success,
    hospital_detail, doctor_detail, hospital_dashboard, maternal_monitoring_list, maternal_monitoring_create,
    common_login
)

urlpatterns = [

    # Home Page
    path("", index, name="index"),
    
    #common login page
    path("login/", common_login, name="common_login"),

    # Registration URLs
    path("register/", register_hospital, name="register_hospital"),
    path("register/doctor/", register_doctor, name="register_doctor"),
    path("register/patient/", register_patient, name="register_patient"),
    path("register/intern/", register_intern, name="register_intern"),

    # Success pages
    path("patient/success/", patient_success, name="patient_success"),
    path("intern/success/", intern_success, name="intern_success"),

    # Doctor URLs
    path("doctor/dashboard/", doctor_dashboard, name="doctor_dashboard"),
    path("doctor/login/", doctor_login, name="doctor_login"),
    path("doctor/logout/", LogoutView.as_view(next_page="doctor_login"), name="doctor_logout"),

    # Hospital Dashboard and Details
    path("dashboard/", hospital_dashboard, name="hospital_dashboard"),
    path("hospital/<int:hospital_id>/", hospital_detail, name="hospital_detail"),
    path("doctor/<int:doctor_id>/", doctor_detail, name="doctor_detail"),

    # Maternal Monitoring
    path("maternal-monitoring/", maternal_monitoring_list, name="maternal_monitoring_list"),
    path("maternal-monitoring/add/", maternal_monitoring_create, name="maternal_monitoring_create"),
]
