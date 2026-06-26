from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            return render(request, 'accounts/register.html', {'error': 'Пароли не совпадают'})
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Пользователь уже существует'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employees:list')
        return render(request, 'accounts/login.html', {'error': 'Неверное имя пользователя или пароль'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
