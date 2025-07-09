
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('home/',views.index, name='index'),
    path('',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('starter/',views.starter, name='starter'),
    path('about/',views.about, name='about'),
    path('services/',views.services, name='services'),
    path('doctors/',views.doctors, name='doctors'),
    path('appointment/',views.appointment, name='appointment'),
    path('contact/',views.contact, name='contact'),
    path('show/',views.show, name='show'),
    path('display/',views.display, name='display'),
    path('edit/<int:id>',views.edit, name='edit'),

    path('delete/<int:id>',views.delete),
]
