from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic.base import View
from ..models import *


class SignIn(View):
    """登陆页面"""

    def get(self, request):
        return render(request, 'sign_in.html', context=None)

    def post(self, request):
        _user = request.POST['user']
        _pwd = request.POST['pwd']
        user = authenticate(username=_user, password=_pwd)
        if user is not None:
            login(request, user)
            return redirect('/blog/')
        else:
            return redirect('/blog/sign_up/')


class SignUp(View):
    """注册页面"""

    def get(self, request):
        return render(request, 'sign_up.html', context=None)

    def post(self, request):
        user = request.POST['user']
        pwd = request.POST['pwd']
        # create_user方法自动save
        user_sign_up = User.objects.create_user(username=user, email=None, password=pwd)

        return redirect('/blog/sign_in/')


class SignOut(View):
    """登出页面"""

    def get(self, request):
        logout()
        return redirect('/blog/sign_in/')
