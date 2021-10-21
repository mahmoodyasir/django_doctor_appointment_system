from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUserForm, UpdateForm
from .models import PatientInfo, BookAppointment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from doctor .models import Appointment


# Create your views here.

@login_required(login_url='login-register')
def patient_index(request):
    return render(request, "patientfile/patient_index.html")


def register_patient(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='patient')
            user.groups.add(group)
            PatientInfo.objects.create(
                user=user,
                name=user.username,
                email=user.email,
                phone=" ",
                age=0,
                address=" ",
            )

            messages.success(request, 'Account was created for '+username)
    return render(request, "login_register.html", context)


def patient_info(request, pk):
    info = PatientInfo.objects.get(id=pk)
    if not info.user == request.user:
        return HttpResponseForbidden("No Access")
    cursor = {"info": info}
    return render(request, "patientfile/patient_info.html", cursor)


@login_required(login_url='login-register')
def patient_update_info(request, pk):
    update = PatientInfo.objects.get(id=pk)
    if not update.user == request.user:
        return HttpResponseForbidden("No Access")
    cursor = {"update": update}
    return render(request, "patientfile/patient_update_form.html", cursor)


@login_required(login_url='login-register')
def patient_final_update(request, pk):
    f_update = PatientInfo.objects.get(id=pk)
    if not f_update.user == request.user:
        return HttpResponseForbidden("No Access")
    form = UpdateForm(instance=f_update)

    # if request.method == 'GET':
    #     form = UpdateForm(instance=f_update)
    #     return redirect('home')

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=f_update)
        if form.is_valid():
            form.save()
            return redirect('patient-home')


def your_appointment(request, pk):
    temp_id = Appointment.objects.get(id=pk)
    doc_id = temp_id.doctor_id
    doc_name = doc_id.doctorinfo.name

    p_id = request.user
    ranges = temp_id.total_patient
    serial = temp_id.enrolled_patient
    increment = serial + 1

    date = temp_id.date_created
    s_time = temp_id.start_time
    e_time = temp_id.end_time
    temp1 = BookAppointment.appointment_id
    temp2 = temp_id.id
    print(temp1)
    print(" ")
    print(temp2)

    if temp1 == temp2:
        return HttpResponse("Doesn't Work")

    else:

        if ranges >= increment:
            temp_id.enrolled_patient = increment

            BookAppointment.objects.create(
                appointment_id=temp_id.id,
                patient_id=p_id,
                doctor_id=doc_id,
                doctor_name=doc_name,
                serial=increment,
                date_created=date,
                start_time=s_time,
                end_time=e_time,
                checker=1,
            )

            temp_id.save()

            cursor = {"doc_name": doc_name, "date": date, "increment": increment, "s_time": s_time, "e_time": e_time}
            return render(request, "patientfile/your_appointment.html", cursor)
    messages.success(request, 'Slot already full')







