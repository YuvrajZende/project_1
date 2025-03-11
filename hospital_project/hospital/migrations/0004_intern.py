# Generated by Django 5.1.7 on 2025-03-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('aadhaar', models.CharField(max_length=12, unique=True)),
                ('pan', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('graduation_year', models.IntegerField()),
                ('university', models.CharField(max_length=255)),
                ('registration_number', models.CharField(blank=True, max_length=100, null=True)),
                ('council_name', models.CharField(blank=True, max_length=255, null=True)),
                ('internship_hospital', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('training', models.TextField(blank=True, null=True)),
                ('interest', models.TextField(blank=True, null=True)),
                ('work_experience', models.TextField(blank=True, null=True)),
                ('availability', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], max_length=20)),
                ('shift_preference', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Flexible', 'Flexible')], max_length=20)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('emergency_contact', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=255)),
                ('resume', models.FileField(upload_to='intern_resumes/')),
                ('id_proof', models.FileField(upload_to='intern_id_proofs/')),
                ('consent', models.BooleanField(default=False)),
            ],
        ),
    ]
