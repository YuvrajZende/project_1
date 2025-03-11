from django.shortcuts import render, redirect
from .forms import HospitalForm , DoctorForm, PatientForm, InternForm

""" hospital registration view"""

def register_hospital(request):
    if request.method == "POST":
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")  # Make sure this matches the URL pattern name
 # Redirect after submission
    else:
        form = HospitalForm()
    
    return render(request, "hospital/register.html", {"form": form}) #http://127.0.0.1:8000/hospital/register/

def success_page(request):
    return render(request, 'hospital/success.html') 


""" doctor registration view"""

def register_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("doctor_success")      
    else:
        form = DoctorForm()
    
    return render(request, "hospital/doctor_register.html", {"form": form})   # http://127.0.0.1:8000/hospital/register/doctor/

def doctor_success(request):
    return render(request, 'hospital/doctor_success.html') # http://127.0.0.1:8000/hospital/doctor/success/


""" patient registration view"""

def register_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient_success")
    else:
        form = PatientForm()
    
    return render(request, "hospital/patient_register.html", {"form": form}) #http://127.0.0.1:8000/hospital/register/patient/

def patient_success(request):
    return render(request, 'hospital/patient_success.html')


def register_intern(request):
    if request.method == "POST":
        form = InternForm(request.POST, request.FILES)  # Handling file uploads
        if form.is_valid():
            form.save()
            return redirect("intern_success")  # Redirect to success page
    else:
        form = InternForm()
    
    return render(request, "hospital/intern_register.html", {"form": form}) #http://127.0.0.1:8000/hospital/register/intern/

def intern_success(request):
    return render(request, 'hospital/intern_success.html')
