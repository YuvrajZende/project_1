from django.db import models



""" details of the hospital model """

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    operating_name = models.CharField(max_length=255, blank=True, null=True)
    hospital_type = models.CharField(max_length=50, choices=[
        ("General", "General"), ("Specialty", "Specialty"),
        ("Teaching", "Teaching"), ("Private", "Private"), ("Public", "Public")
    ])
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    establishment_date = models.DateField()
    address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)
    accreditation_status = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")])
    accrediting_body = models.CharField(max_length=100, blank=True, null=True)
    emergency_services = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")])
    operating_hours = models.CharField(max_length=100)
    telemedicine = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")])
    owner_name = models.CharField(max_length=255)
    admin_name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=100)
    funding_type = models.CharField(max_length=50, choices=[("Public", "Public"), ("Private", "Private"), ("Non-Profit", "Non-Profit")])
    license_number = models.CharField(max_length=100)
    
    # Relationships
    doctors = models.ManyToManyField("Doctor", related_name="hospitals", blank=True)
    patients = models.ManyToManyField("Patient", related_name="hospitals", blank=True)
    interns = models.ManyToManyField("Intern", related_name="hospitals", blank=True)

    def __str__(self):
        return self.hospital_name




""" details of the doctor model"""

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100, choices=[
        ("Cardiology", "Cardiology"), ("Neurology", "Neurology"),
        ("Pediatrics", "Pediatrics"), ("Dermatology", "Dermatology")
    ])
    license_number = models.CharField(max_length=100, unique=True)
    aadhaar = models.CharField(max_length=12, unique=True)
    pan = models.CharField(max_length=10, unique=True)
    experience = models.IntegerField()
    current_hospital = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Store securely using Django's authentication system
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    dob = models.DateField()
    qualification = models.CharField(max_length=255)
    med_council_reg = models.CharField(max_length=100)
    clinic_hospital = models.CharField(max_length=255, blank=True, null=True)
    years_practice = models.IntegerField()
    consultation_fee = models.IntegerField(blank=True, null=True)
    working_hours = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=15)
    alternate_contact = models.CharField(max_length=255, blank=True, null=True)
    languages = models.TextField()
    documents = models.FileField(upload_to='doctor_documents/', blank=True, null=True)
    profile_photo = models.ImageField(upload_to='doctor_photos/', blank=True, null=True)
    consent = models.BooleanField(default=False)
    

    patients = models.ManyToManyField("Patient", related_name="doctors", blank=True)
    interns = models.ManyToManyField("Intern", related_name="mentors", blank=True)


    def __str__(self):
        return self.name
    
    
    

""" details of the patient model"""


class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    dob = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, unique=True)
    alt_phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    marital_status = models.CharField(max_length=50, choices=[
        ("Married", "Married"), ("Single", "Single"),
        ("Widow", "Widow"), ("Divorced", "Divorced"), ("Other", "Other")
    ])
    blood_group = models.CharField(max_length=5, choices=[
        ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")
    ])
    
    # Emergency Contact
    emergency_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=15)

    # Pregnancy Information
    pregnant = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True)
    months_pregnant = models.IntegerField(blank=True, null=True)
    edd = models.DateField(blank=True, null=True)
    first_pregnancy = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True)
    previous_pregnancies = models.IntegerField(blank=True, null=True)
    miscarriages = models.IntegerField(blank=True, null=True)
    children_delivered = models.IntegerField(blank=True, null=True)
    lmp = models.DateField(blank=True, null=True)
    complications = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True)
    complication_details = models.TextField(blank=True, null=True)

    # Medical History
    ongoing_medications = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True)
    medication_details = models.TextField(blank=True, null=True)
    allergies = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True)
    allergy_details = models.TextField(blank=True, null=True)
    family_history = models.TextField(blank=True, null=True)

    # Insurance
    insurance = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True)
    insurance_provider = models.CharField(max_length=255, blank=True, null=True)
    policy_number = models.CharField(max_length=100, blank=True, null=True)
    coverage_details = models.TextField(blank=True, null=True)

    # Dietary Preferences
    dietary_preference = models.CharField(max_length=20, choices=[("Vegetarian", "Vegetarian"), ("Non-Vegetarian", "Non-Vegetarian")])

    # Caste & Religion (Optional)
    caste = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)

    #interns = models.ManyToManyField(Intern, related_name='patients')

    def __str__(self):
        return self.full_name
    

""" details of the intern model """

class Intern(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    aadhaar = models.CharField(max_length=12, unique=True)
    pan = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255)  # Store securely using Django's authentication system

    # Academic & Professional Details
    qualification = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    university = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    council_name = models.CharField(max_length=255, blank=True, null=True)
    internship_hospital = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    experience = models.IntegerField()
    training = models.TextField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)

    # Work & Availability
    work_experience = models.TextField(blank=True, null=True)
    availability = models.CharField(max_length=20, choices=[("Full-time", "Full-time"), ("Part-time", "Part-time")])
    shift_preference = models.CharField(max_length=20, choices=[("Day", "Day"), ("Night", "Night"), ("Flexible", "Flexible")])

    # Personal Information
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    emergency_contact = models.CharField(max_length=15)
    location = models.CharField(max_length=255)

    # Documents
    resume = models.FileField(upload_to='intern_resumes/')
    id_proof = models.FileField(upload_to='intern_id_proofs/')
    consent = models.BooleanField(default=False)

    #patients = models.ManyToManyField('Patient', related_name='interns')
    
    def __str__(self):
        return self.name

# input from the user

class MaternalMonitoring(models.Model):
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name="maternal_monitoring")
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="maternal_monitoring")
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.CharField(max_length=20)
    fetal_heart_rate = models.CharField(max_length=20)
    temperature = models.CharField(max_length=10)
    monitoring_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.monitoring_date}"