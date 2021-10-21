# Generated by Django 3.2.6 on 2021-08-17 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=150)),
                ('usage_per_day', models.TextField()),
                ('total_duration', models.CharField(max_length=150)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctorinfo')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=150)),
                ('institution', models.CharField(max_length=150)),
                ('year_of_degree', models.DateField()),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctorinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('total_patient', models.IntegerField()),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctorinfo')),
            ],
        ),
    ]
