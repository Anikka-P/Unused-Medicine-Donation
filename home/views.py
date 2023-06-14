from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
from home.models import Userdonor,Userngo,Donations
from django.contrib import messages
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# View creation
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def signupdonor(request):
    return render(request, 'signupdonor.html')

def signupngo(request):
    return render(request, 'signupngo.html') 

def login(request):
    return render(request, 'login.html') 

def donationform(request):
    return render(request, 'donationform.html') 

def ourteam(request):
    return render(request, 'ourteam.html') 

def listofdonors(request):
    alldonors=Donations.objects.filter(accepted_by="None")
    value=request.POST.get('ngokanaam')
    email=request.POST.get('email')
    return render(request, 'listofdonors.html',{'donorlist':alldonors,'variable':value,'variable1':email}) 

def accept(request):
    id_no=request.POST.get('accepting')
    naam=request.POST.get('ngokanaam')
    print(naam)
    email=request.POST.get('email')
    print(email)
    Donations.objects.filter(id=id_no).update(accepted_by=naam)
    r=Donations.objects.get(id=id_no)
    return render(request, 'welcomengo.html',{"variable":naam,"variable1":email}) 
    
def donorhistory(request):
    value=request.POST.get("donorkaemail")
    alldata=Donations.objects.filter(email=value)
    return render(request,'donorhistory.html',{'donorlist':alldata})
    
def ngohistory(request):
    value=request.POST.get("ngokanaam")
    alldata=Donations.objects.filter(accepted_by=value)
    print(alldata)
    return render(request,'ngohistory.html',{'donorlist':alldata})

def welcomedonor(request):
    value=request.POST.get('myemail')
    data=Userdonor.objects.filter(email=value)
    for i in data:
        value2=i.name
    return render(request,'welcomedonor.html',{"variable":value2,"variable1":value})

def welcomengo(request):
    value=request.POST.get('myemail')
    data=Userngo.objects.filter(email=value)
    for i in data:
        value2=i.name
    return render(request,'welcomengo.html',{"variable":value2,"variable1":value})

def updatedonor(request):
    newname=request.POST.get('newname')
    newphone=request.POST.get('newphone')
    newemail=request.POST.get('newemail')
    value=request.POST.get('updateinformation')
    if(newname!=""):
        Userdonor.objects.filter(email=value).update(name=newname)
        Donations.objects.filter(email=value).update(donor_name=newname)
    if(newphone!=""):
        Userdonor.objects.filter(email=value).update(phone=newphone)
        Donations.objects.filter(email=value).update(phone=newphone)
    if(newemail!=""):
        Userdonor.objects.filter(email=value).update(email=newemail)
        Donations.objects.filter(email=value).update(email=newemail)
    if newemail=="":
        data=Userdonor.objects.filter(email=value)
        for i in data:
            value2=i.name
    else:
        data=Userdonor.objects.filter(email=newemail)
        for i in data:
            value2=i.name
        value=newemail
    return render(request,'welcomedonor.html',{"variable":value2,"variable1":value})

def updatengo(request):
    newname=request.POST.get('newname')
    newphone=request.POST.get('newphone')
    newemail=request.POST.get('newemail')
    newaddress=request.POST.get('newaddress')
    newcertification=request.POST.get('newcertification')
    purananaam=request.POST.get('oldname')
    value=request.POST.get('updateinformation')
    if(newname!=""):
        Userngo.objects.filter(email=value).update(name=newname)
        Donations.objects.filter(email=value).update(donor_name=newname)
        Donations.objects.filter(accepted_by=purananaam).update(accepted_by=newname)
    if(newphone!=""):
        Userngo.objects.filter(email=value).update(phone=newphone)
    if(newaddress!=""):
        Userngo.objects.filter(email=value).update(address=newaddress)
    if(newcertification!=""):
        Userngo.objects.filter(email=value).update(certification=newcertification)
    if(newemail!=""):
        Userngo.objects.filter(email=value).update(email=newemail)
    if newemail=="":
        data=Userngo.objects.filter(email=value)
        for i in data:
            value2=i.name
    else:
        data=Userngo.objects.filter(email=newemail)
        for i in data:
            value2=i.name
        value=newemail
    return render(request,'welcomengo.html',{"variable":value2,"variable1":value})


def donorprofileopen(request):
    value=request.POST.get('profile')
    data=Userdonor.objects.filter(email=value)
    return render(request,'donorprofile.html',{'donorfields':data})

def ngoprofileopen(request):
    value=request.POST.get('profile')
    data=Userngo.objects.filter(email=value)
    return render(request,'ngoprofile.html',{'ngofields':data})

def logincheck(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    loginas=request.POST.get('loginas')
    if loginas=="DONOR":
        user = authenticate(email=email, password=password)
        data=Userdonor.objects.all()
        e={}
        f={}
        for i in data:
            e[i.email]=i.password
            f[i.email]=i.name
        if email in e:
            if check_password(password,e[email]):  
                return render(request,'welcomedonor.html',{"variable":f[email],"variable1":email})
            else:
                return render(request,'login.html',{"variable1":"Email-id and password do not match.."})
        else:
            return render(request,'login.html',{"variable1":"Email-id does not exists.."})
    elif loginas=="NGO":
        data=Userngo.objects.all()
        e={}
        f={}
        for i in data:
            e[i.email]=i.password
            f[i.email]=i.name
        if email in e:
            if check_password(password,e[email]):
                return render(request,'welcomengo.html',{"variable":f[email],"variable1":email})
            else:
                return render(request,'login.html',{"variable1":"Email-id and password do not match.."})
        else:
            return render(request,'login.html',{"variable1":"Email-id does not exists.."})

def saveuserdonor(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    a=0
    data=Userdonor.objects.all()
    z=0
    for i in data:
        if i.email==email:
            z=1
            break
    if z==1:
        return render(request,'signupdonor.html',{"variable":"Email id already exists"})
    for i in phone:
        if ord(i)<48 or ord(i)>57:
            a=1
            break
    if a==1 or len(phone)!=10:
        return render(request,'signupdonor.html',{"variable":"Mobile no. should contain 10 digits only"})
    if not (re.search(regex,email)):
        return render(request,'signupdonor.html',{"variable":"Invalid email-id"})
    password = request.POST.get('password')
    confirmpassword=request.POST.get('confirmpassword')
    if password!=confirmpassword:
        return render(request,'signupdonor.html',{"variable":"Passwords do not match"})
    encrypted=make_password(password)
    user = Userdonor(name=name, email=email, phone=phone,password=encrypted)
    user.save()
    return render(request,'welcomedonor.html',{"variable":name,"variable1":email})

def saveuserngo(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    a=0
    data=Userngo.objects.all()
    z=0
    for i in data:
        if i.email==email:
            z=1
            break
    if z==1:
        return render(request,'signupngo.html',{"variable":"Email id already exists"})
    for i in phone:
        if ord(i)<48 or ord(i)>57:
            a=1
            break
    if a==1 or len(phone)!=10:
        return render(request,'signupngo.html',{"variable":"Mobile no. should contain 10 digits only"})
    if not (re.search(regex,email)):
        return render(request,'signupngo.html',{"variable":"Invalid email-id"})
    password = request.POST.get('password')
    confirmpassword=request.POST.get('confirmpassword')
    address = request.POST.get('address')
    certification = request.POST.get('certification')
    if password!=confirmpassword:
        return render(request,'signupngo.html',{"variable":"Passwords do not match"})
    encrypted=make_password(password)
    user = Userngo(name=name, email=email, phone=phone,password=encrypted,address=address,certification=certification)
    user.save()
    context={
        "variable":name,
        "variable1":email
    }
    return render(request,'welcomengo.html',context)

def donations(request):
    donor_name = request.POST.get('donor_name')
    medicine_name = request.POST.get('medicine_name')
    phone = request.POST.get('phone')
    pickup_address = request.POST.get('pickup_address')
    expiry_date = request.POST.get('expiry_date')
    purpose = request.POST.get('purpose')
    accepted_by=request.POST.get('accepted_by',default="None")
    email=request.POST.get('email')
    user = Donations(donor_name=donor_name, medicine_name=medicine_name, phone=phone,pickup_address=pickup_address, expiry_date=expiry_date,purpose=purpose,accepted_by=accepted_by,email=email)
    user.save()
    return render(request,'welcomedonor.html',{"variable":donor_name,"variable1":email})