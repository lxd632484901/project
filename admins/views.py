from alipay import AliPay
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# from pip._vendor.requests import Response

from store.models import User
from storeproject.settings import ALI_APP_ID, APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY


def index(request):
    if request.POST:
        passwd = request.POST.get('password', '')
        usernm = request.POST.get('username', '')
        user = authenticate(username=usernm, password=passwd)
        if user:
            if user.is_superuser:
                if user.is_active:
                    login(request, user)
                    return render(request,'admin/index.html')
                return HttpResponse('<script>alert("账户已被锁定无法登录！");history.go(-2)</script>')
            return HttpResponse('<script>alert("不是管理员！");history.go(-2)</script>')
        return HttpResponse('<script>alert("账号或者密码错误");history.back()</script>')
    return render(request, 'adminlogin.html', locals())





