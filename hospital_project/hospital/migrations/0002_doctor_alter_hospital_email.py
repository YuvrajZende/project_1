# Generated by Django 5.1.7 on 2025-03-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('specialization', models.CharField(choices=[('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Pediatrics', 'Pediatrics'), ('Dermatology', 'Dermatology')], max_length=100)),
                ('license_number', models.CharField(max_length=100, unique=True)),
                ('aadhaar', models.CharField(max_length=12, unique=True)),
                ('pan', models.CharField(max_length=10, unique=True)),
                ('experience', models.IntegerField()),
                ('current_hospital', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('dob', models.DateField()),
                ('qualification', models.CharField(max_length=255)),
                ('med_council_reg', models.CharField(max_length=100)),
                ('clinic_hospital', models.CharField(blank=True, max_length=255, null=True)),
                ('years_practice', models.IntegerField()),
                ('consultation_fee', models.IntegerField(blank=True, null=True)),
                ('working_hours', models.CharField(max_length=100)),
                ('emergency_contact', models.CharField(max_length=15)),
                ('alternate_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('languages', models.TextField()),
                ('documents', models.FileField(blank=True, null=True, upload_to='doctor_documents/')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='doctor_photos/')),
                ('consent', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='hospital',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
