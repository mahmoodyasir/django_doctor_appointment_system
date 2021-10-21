from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse

from .models import *
from django.shortcuts import get_object_or_404
from .forms import UpdateForm, AppointmentForm, CreateAppointmentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect


# Create your views here.
def general(request):
    return render(request, 'general.html')


@login_required(login_url='login-register')
def index(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "patient":
        return HttpResponseRedirect(reverse('patient-home'))
    elif group.name == "doctor":
        return render(request, "index.html")


@login_required(login_url='login-register')
def doc_info(request, pk):
    info = DoctorInfo.objects.get(id=pk)
    if not info.user == request.user:
        return HttpResponseForbidden("No Access")
    cursor = {"info": info}
    return render(request, "doctor_info.html", cursor)


@login_required(login_url='login-register')
def doc_update_info(request, pk):
    update = DoctorInfo.objects.get(id=pk)
    if not update.user == request.user:
        return HttpResponseForbidden("No Access")
    cursor = {"update": update}
    return render(request, "doc_update_form.html", cursor)


@login_required(login_url='login-register')
def doc_final_update(request, pk):
    f_update = DoctorInfo.objects.get(id=pk)
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
            return redirect('doctor-home')


@login_required(login_url='login-register')
def doctor_appointment(request, pk):

    user_update = DoctorInfo.objects.get(id=pk)
    print(user_update)
    if not user_update.user == request.user:
        return HttpResponseForbidden("No Access")
    user_name = user_update.user
    apt_update = Appointment.objects.filter(doctor_id=user_name)
    # print(apt_update)
    cursor = {"apt_update": apt_update}
    print(cursor)
    return render(request, 'doc_appointment.html', cursor)
    # args = {}
    # args['user_profile'] = User.objects.get(username=user_login_name)
    # return render(request, 'doc_appointment.html', args)


def doctor_appointment_update(request, pk):
    print(pk)
    apt_update = Appointment.objects.filter(id=pk).first()
    print(apt_update)
    # if not user_update.user == request.user:
    #     return HttpResponseForbidden("No Access")
    # user_name = user_update.user
    # apt_update = Appointment.objects.filter(doctor_id=user_name).first()

    form = AppointmentForm(instance=apt_update)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=apt_update)
        if form.is_valid():
            form.save()
            return redirect('doctor-home')


@login_required(login_url='login-register')
def doctor_appointment_form(request, pk):
    user_update = DoctorInfo.objects.get(id=pk)
    print(user_update)
    if not user_update.user == request.user:
        return HttpResponseForbidden("No Access")
    return render(request, 'create_appointment.html')


@login_required(login_url='login-register')
def doctor_appointment_create(request, pk):
    doctor_id = User.objects.get(id=pk)
    cursor = {"id": pk}

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.doctor_id = doctor_id
            appointment.save()
            return HttpResponseRedirect(reverse('doctor-appointment', kwargs={'pk': pk}))
        return HttpResponseRedirect(reverse('doctor-home'))


@login_required(login_url='login-register')
def doc_appointment_delete(request, pk):
    appointment = Appointment.objects.get(id=pk)
    user_id = request.user
    pk = user_id.id
    if not appointment.doctor_id == request.user:
        return HttpResponse("Doesn't Work")
    appointment.delete()
    return HttpResponseRedirect(reverse('doctor-appointment', kwargs={'pk': pk}))


def login_register_page(request):
    return render(request, "login_register.html")


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('doctor-home')
        else:
            messages.info(request, 'Username or Password is invalid')

    cursor = {}
    return render(request, 'login_register.html', cursor)


def doctor_logout(request):
    logout(request)
    return redirect('login-register')


def take_appointment(request):
    app_info = DoctorInfo.objects.all()
    cursor = {"app_info": app_info}
    return render(request, "patientfile/take_appointment.html", cursor)


def patient_appointment(request, pk):
    doc_id = DoctorInfo.objects.get(id=pk)
    app_info = DoctorInfo.objects.get(id=pk)

    user_name = doc_id.user
    apt_id = Appointment.objects.filter(doctor_id=user_name)

    cursor = {"apt_id": apt_id, "app_info": app_info}
    return render(request, "patientfile/patient_appointment.html", cursor)


