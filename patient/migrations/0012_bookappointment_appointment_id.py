# Generated by Django 3.2.6 on 2021-10-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_auto_20211020_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappointment',
            name='appointment_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
