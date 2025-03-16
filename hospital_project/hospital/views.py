from django.shortcuts import render, redirect, get_object_or_404
from .forms import HospitalForm , DoctorForm, PatientForm, InternForm, MaternalMonitoringForm
from .models import MaternalMonitoring, Hospital, Doctor, Patient,Intern
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    return render(request, 'hospital/index.html')

""" hospital registration view"""

from .models import Hospital, Doctor, Patient, Intern
# Redirect to the dashboard after registering a hospital
def register_hospital(request):
    if request.method == "POST":
        form = HospitalForm(request.POST)
        if form.is_valid():
            hospital = form.save()
            return redirect("hospital_dashboard")  # Redirect to dashboard
    else:
        form = HospitalForm()
    return render(request, "hospital/register.html", {"form": form})

# Show hospitals in the dashboard
def hospital_dashboard(request):
    hospitals = Hospital.objects.all()
    return render(request, "hospital/hospital_dashboard.html", {"hospitals": hospitals})

# Show hospital details with doctors & interns
def hospital_detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    doctors = hospital.doctors.all()
    interns = hospital.interns.all()
    return render(request, "hospital/hospital_detail.html", {"hospital": hospital, "doctors": doctors, "interns": interns})

# Show doctor details with patients
def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    patients = doctor.patients.all()
    return render(request, "hospital/doctor_detail.html", {"doctor": doctor, "patients": patients})




""" doctor registration view"""

def register_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save()  # Save the doctor instance
            return redirect("doctor_dashboard")  # Redirect to doctor dashboard after registration
    else:
        form = DoctorForm()
    
    return render(request, "hospital/doctor_register.html", {"form": form})

@login_required
def doctor_dashboard(request):
    return render(request, "hospital/doctor_dashboard.html")  # Render doctor-page.html

def doctor_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("doctor_dashboard")  # Redirect to the Doctor Dashboard after login
        else:
            return render(request, "hospital/doctor_login.html", {"error": "Invalid username or password"})
    return render(request, "hospital/doctor_login.html")



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



def maternal_monitoring_list(request):
    maternal_data = MaternalMonitoring.objects.all()
    return render(request, 'hospital/maternal_monitoring_list.html', {'maternal_data': maternal_data})

def maternal_monitoring_create(request):
    if request.method == "POST":
        form = MaternalMonitoringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maternal_monitoring_list')
    else:
        form = MaternalMonitoringForm()
    return render(request, 'hospital/maternal_monitorization.html', {'form': form})


""" linking for common login page for all  """

def common_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            
            # Redirect based on user type
            if Hospital.objects.filter(email=email).exists():
                return redirect("hospital_dashboard")
            elif Doctor.objects.filter(email=email).exists():
                return redirect("doctor_dashboard")
            elif Patient.objects.filter(email=email).exists():
                return redirect("patient_dashboard")
            elif Intern.objects.filter(email=email).exists():
                return redirect("intern_dashboard")
            else:
                return redirect("index")  # Fallback in case no match
            
        else:
            return render(request, "hospital/common_login.html", {"error": "Invalid credentials"})
    
    return render(request, "hospital/common_login.html")
