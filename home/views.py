from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Registration, Login, Entry, Restaurant
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# create views
from django.forms import inlineformset_factory

# from django.contrib.auth.forms import RegistrationForm
from .forms import RegistrationForm

from django.http import HttpResponse, FileResponse
import io
import os
import csv
from io import BytesIO
     

# Create your views here.
def Index(request):
    return render(request, 'indexnew.html')

def Loginuser(request):
    if request.method == "POST":
       
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            return redirect('indexnew')
        else: 
            messages.info(request, 'Username OR password is incorrect')
    
    context = {}
    return render(request, 'login.html', context)
                

def logoutUser(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('indexnew')

def Indexnew(request):
    
    return render(request, 'indexnew.html')

@login_required(login_url='login')
def Fronts(request):
    # entry = Entry.objects.all()
    if request.method == "POST":
        assetname = request.POST.get('assetname')
        assetserialNo = request.POST.get('assetserialNo')
        assetmanufacturer = request.POST.get('assetmanufacturer')
        date = request.POST.get('date')
        dropdown = request.POST.get('dropdown')
        print('manan')
        data = Entry(assetname=assetname, assetserialNo=assetserialNo, assetmanufacturer=assetmanufacturer, date=date,dropdown=dropdown)
        data.save()
        return redirect('indexnew')
    
    return render(request, 'front.html')

def add(request):
    if request.method == 'POST':
        assetname = request.POST['assetname']
        assetserialNo = request.POST['assetserialNo']
        manu = request.POST['manu']
        date = request.POST['date']
        
        asset = Entry(assetname=assetname, assetserialNo=assetserialNo, assetmanufacturer=manu, date=date)
        asset.save()

    return redirect(modalUser)

def update(request, id):
    id = int(id)
    fetched_asset = Entry.objects.get(id = id)
    if request.method == 'POST':
        assetname = request.POST['assetname']
        assetserialNo = request.POST['assetserialNo']
        manu = request.POST['manu']
        date = request.POST['date']

        fetched_asset.assetname = assetname
        fetched_asset.assetserialNo = assetserialNo
        fetched_asset.manu = manu
        fetched_asset.date = date

        fetched_asset.save()

    return redirect(modalUser)

def delete(request, id):
    id = int(id)
    fetched_asset = Entry.objects.get(id = id)
    fetched_asset.delete()
    return redirect(modalUser)

def Restaurants(request):
    if request.method == "POST":
        Date_of_Purchase = request.POST('Date_of_Purchase')
        No_of_Dishes = request.POST('No_of_Dishes')
        No_of_Spoon = request.POST('No_of_Spoon')
        Water_bottles = request.POST('Water_bottles')
        No_of_Fans = request.POST('No_of_Fans')

        a = Restaurant(Date_of_Purchase=Date_of_Purchase, No_of_Dishes=No_of_Dishes,No_of_Spoon=No_of_Spoon,Water_bottles=Water_bottles,No_of_Fans=No_of_Fans)
        a.save()

    
def Fronts_pdf(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )
    frontss = Entry.objects.all()
     
    final=[]
    Fileds = ['Name', 'Serial Number', 'Manufacturer', 'Dropdown']

    for front in frontss:

        lines=[]
        lines.append(front.assetname)
        lines.append(front.assetserialNo)
        lines.append(front.assetmanufacturer)
        lines.append(front.dropdown)
    
        final.append(lines)

    writer = csv.writer(response)
    writer.writerow(Fileds)
    writer.writerows(final)

    return response

def Registrationpage(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data['fullname']
            username = form.cleaned_data['username']

            user = authenticate(fullname=fullname, username=username)
            user=form.save()
            login(request, user)
            print("manan")
            messages.success(request, 'Account was created')

            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request, 'registration.html',context)

@login_required(login_url='login')
def modalUser(request):
    entry = Entry.objects.all()
    

    return render(request, 'modal.html', {'entry':entry})

# def Registrationpage(request):
#     if request.method == "POST":

#         models = Registration()
#         models.fullname = request.POST.get('fullname')
#         models.username = request.POST.get('username')
#         models.email = request.POST.get('email')
#         models.phonenumber = request.POST.get('phonenumber')
#         models.password = request.POST.get('password')
#         confirmpassword = request.POST.get('confirmpassword')
#         if models.password == confirmpassword:
#             models.save()
#             return redirect('login')
#         else:
#             return render(request, 'registration.html', {'error': 'Password Unmatched'})
#     return render(request, 'registration.html')

# def Registrationpage(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         fullname = request.POST.get('fullname')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phonenumber = request.POST.get('phonenumber')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')
#         user = User.objects.create_user(username=username,email=email,password=password)
#         if user.password == password2:
#             user.save()
#             return redirect('login')
#         else:
#             return render(request, 'registration.html', {'error': 'Password Unmatched'})
#     return render(request, 'registration.html')
