from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm  # Assuming you have a LoginForm
from .forms import RegisterForm
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')  # Redirect to home or another page after login
        else:
            messages.error(request, 'Invalid username or password.')
    
    # If GET request or invalid login attempt
    return render(request, 'user/login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            
            messages.success(request, 'Your account has been created successfully!')
            return redirect('user:login')
        else:
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = RegisterForm()
    
    return render(request, 'user/register.html', {'form': form})