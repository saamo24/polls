from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=username)

        if password == user.password:
            # messages.error(request, 'Invalid email or password.')
            print(password)
            return redirect('/survey/')  
        # login(request)
        return render(request, 'user/login.html', 
                      {'error_message': "Invalid Email or Password"})




def login(request):
    return render(request, 'user/login.html', {'user': request.user})

