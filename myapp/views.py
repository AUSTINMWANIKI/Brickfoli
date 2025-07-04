from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def doctors(request):
    return render(request,'doctors.html')

def appointment(request):
    if request.method=="POST":
       myappointments = Appointment(
            name= request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
             datetime=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
       myappointments.save()
       messages.success(request,'Your appointment has been submitted')
       return redirect('/show')

    else:

        return render(request,'appointment.html')

def contact(request):
    if request.method=="POST":
       mycontacts = Contact(
            name= request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
       mycontacts.save()
       messages.success(request,'Your contact has been submitted')
       return redirect('/contact')

    else:

        return render(request,'contact.html')

def show(request):
    all = Appointment.objects.all()
    return render(request,'show.html',{'all':all})

def delete(request,id):
    myappoint = Appointment.objects.get(id=id)
    myappoint.delete()
    return redirect('/show')

    return render(request,'show.html')

def display(request):
    all = Contact.objects.all()
    return render(request,'display.html',{'all':all})

def delete(request,id):
    myappoint = Contact.objects.get(id=id)
    myappoint.delete()
    return redirect('/display')

    return render(request,'display.html',)

def edit(request,id):
    editappointment = get_object_or_404(Appointment,id=id)

    if request.method=="POST":
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.phone = request.POST.get('phone')
        editappointment.datetime = request.POST.get('date')
        editappointment.department = request.POST.get('department')
        editappointment.doctor = request.POST.get('doctor')
        editappointment.message = request.POST.get('message')

        editappointment.save()
        messages.success(request,'Your appointment has been updated successfully')
        return redirect('/show')

    return render(request,'edit.html',{"editappointment":editappointment})

