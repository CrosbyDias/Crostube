from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'main/home.html', {'user': user})
        else:
            return render(request, 'auth_user/login_user.html', {'error': 'Invalid username or password'})
    return render(request, 'main/home.html')  

def logout_user(request):
    logout(request)
    return redirect(request, 'login_user')
