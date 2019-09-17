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


@login_required(login_url='/')
def base(request):
    # alipay = AliPay(
    #     appid=ALI_APP_ID,
    #     app_notify_url=None,
    #     app_private_key_string=APP_PRIVATE_KEY,
    #     alipay_public_key_string=ALIPAY_PUBLIC_KEY,
    #
    #     sign_type="RSA2",
    #     debug=False
    # )
    # order_string = alipay.api_alipay_trade_page_pay(
    #     out_trade_no="2019061900100",
    #     total_amount=30,
    #     subject="macpro",
    #     return_url="http://localhost:8000/",
    #     notify_url="http://localhost:8000/",
    #
    # )
    #
    # # data = {
    # #     "msg": "ok",
    # #     "status": 200,
    # #     "data": {"pay_url": net + order_string
    # #              }
    # #                          }
    # net = "https://openapi.alipaydev.com/gateway.do?{}".format(order_string)

    logout(request)
    return HttpResponse('as')

