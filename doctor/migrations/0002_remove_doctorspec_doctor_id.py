# Generated by Django 3.2.6 on 2021-08-17 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorspec',
            name='doctor_id',
        ),
    ]