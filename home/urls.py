from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='home'),
    path("about", views.about, name='about'),
    path("signupdonor", views.signupdonor, name='signindonor'),
    path("signupngo", views.signupngo, name='signupngo'),
    path("login", views.login, name='login'),
    path("saveuserdonor", views.saveuserdonor, name='saveuserdonor'),
    path("saveuserngo", views.saveuserngo, name='saveuserngo'),
    path("donations", views.donations, name='donations'),
    path("donationform", views.donationform, name='donationform'),
    path("listofdonors", views.listofdonors, name='listofdonors'), 
    path("ourteam", views.ourteam, name='ourteam'),
    path("logincheck", views.logincheck, name='logincheck'),
    path("donorhistory", views.donorhistory, name='donorhistory'),
    path("ngohistory", views.ngohistory, name='ngohistory'),
    path("accept", views.accept, name='accept'),
    path("donorprofileopen", views.donorprofileopen, name='donorprofileopen'),
    path("ngoprofileopen", views.ngoprofileopen, name='ngoprofileopen'),
    path("welcomedonor", views.welcomedonor, name='welcomedonor'),
    path("welcomengo", views.welcomengo, name='welcomengo'),
    path("updatedonor", views.updatedonor, name='updatedonor'),
    path("updatengo", views.updatengo, name='updatengo'),
]