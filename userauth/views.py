from django.shortcuts import render,redirect,HttpResponse
from userauth import models
from Home import views
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
# Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login, authenticate
# from . import models  # Replace with appropriate module where Account model is defined

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

       
        # Validate input
        has_errors = False
        if not username:
            messages.error(request, "Username is required.", extra_tags='username')
            has_errors = True
        elif len(username) < 5:
            messages.error(request, "Username must be at least 5 characters long.", extra_tags='username')
            has_errors = True
        elif models.Account.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken. Please choose a different username.", extra_tags='username')
            has_errors = True


    
        if not email:
            messages.error(request, "Email is required.", extra_tags='email')
            has_errors = True
        elif "@" not in email:
            messages.error(request, "Enter a valid email address.", extra_tags='email')
            has_errors = True
        elif models.Account.objects.filter(email=email).exists():
            messages.error(request, "This email is already exist. Please choose a different email.", extra_tags='email')
            has_errors = True
        
        if not firstname:
            messages.error(request, "First name is required.", extra_tags='firstname')
            has_errors = True

        if not lastname:
            messages.error(request, "Last name is required.", extra_tags='lastname')
            has_errors=True

        if not phonenumber:
            messages.error(request, "Phone Number is required.", extra_tags='phonenumber')
            has_errors=True
        elif len(phonenumber)!=10:
            messages.error(request, "Phone Number must be 10 digits.", extra_tags='phonenumber')
            has_errors=True
        elif models.Account.objects.filter(phone_number=phonenumber).exists():
            messages.error(request, "Phone Number  is already exist,please choose another one.", extra_tags='phonenumber')
            has_errors=True
        
        if not password:
            messages.error(request, "Password is required.", extra_tags='password')
            has_errors = True
        elif len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.", extra_tags='password')
            has_errors = True
        elif password!=  password2: 
            messages.error(request, "Passwords do not match.", extra_tags='password')
            has_errors = True   
        
        if has_errors:
            context = {
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'phonenumber': phonenumber,
                'password':password,
                'password2':password2,
            }
            return render(request, 'register.html', context=context)

         

        # Create user
        user = models.Account.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, phone_number=phonenumber, password=password)
        
        # Authenticate and log in user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully registered and logged in.")
            return redirect('home')  # Redirect to home page after successful registration and login
        else:
            messages.error(request, "Failed to authenticate user.")
            return redirect('register')  # Redirect to register page if authentication fails

    return render(request, "register.html")





def signin(request):
    if request.method =='POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password,)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request,"You are successfully logged in")
                return redirect('home')
            
        else:
            messages.warning(request,"invalid username or password")
        
      
    return render(request, "signin.html")

@login_required
def signout(request):
    logout(request)
    messages.success(request,"You are successfully loggedout")
    return redirect('signin')

# @login_required(login_url='signin')
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context=context)