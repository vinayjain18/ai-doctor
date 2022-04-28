from django.shortcuts import render, redirect
from .forms import ProfileForm, createUserForm
from .models import Appointment, Profile
from random import choice
from string import ascii_letters
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        mobile = request.POST.get("phone")

        appointment = Appointment(first_name=first_name, last_name=last_name, email=email, mobile=mobile)
        appointment.save()
        return redirect("/")

    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        username = User.objects.filter(email=email).exists()
        if username:
            print(username)
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                #login(request, user)
                return redirect("/")
            else:
                return redirect("/sign-up")

        else:
            messages.error(request,"Email Id doesn\'t exist, Please Register")
            return redirect("/login")


        #return render(request, "login.html")

    return render(request, "login.html")


def sign_up(request):
    user = createUserForm()
    form = ProfileForm()
    if request.method == 'POST':
        user = createUserForm(request.POST)
        form = ProfileForm(request.POST)

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        user = User.objects.filter(email=email).exists()

        username = ''.join([choice(ascii_letters) for i in range(30)])

        if password1 != password2:
            messages.error(request, "Both Password are different")
            return redirect("/sign-up")
        
        elif user:
            messages.error(request, "User with this email id already exists.")
            return redirect("/sign-up")

        else:
            new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
            new_user.save()
            
            form = Profile(user=new_user, gender=gender, mobile=mobile, age=age)
            form.save()

            username = User.objects.get(email=email)
            user = authenticate(username=username, password=password1)
            if user is not None:
                auth.login(request, user)
            

        return redirect("/")

    else:
        form = ProfileForm()
        user = createUserForm()

    context = {'form':form, 'user_form': user}
    return render(request, "signup.html", context)


def logout(request):
    logout(request)