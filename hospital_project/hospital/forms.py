from django import forms
from .models import Hospital,Doctor,Patient,Intern

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'     
        
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'   

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'