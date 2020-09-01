from django.shortcuts import render, redirect
from .forms.login import LoginForm, RegisterForm
from django.http import HttpResponse, JsonResponse
from .models import User, Portfolio, Asset, tData
from django.contrib.auth import logout
import time
import os
import random
# from django.conf import settings
from Django import settings
import csv,json
# Create your views here.


def advantage(request):
    username = request.session.get("username", "未登录")
    userimg = request.session.get("userimg", "../../static/assets/images/users/user-4.jpg")
    # return render(request, 'center.html', {"userimg": userimg, "username":username}, locals())
    return render(request, 'advantage.html', locals())
def index(request):
    username = request.session.get("username", "未登录")
    userimg = request.session.get("userimg", "../../static/assets/images/users/user-4.jpg")
    return render(request, 'index.html', {"username": username, "userimg": userimg}, locals())
def combination(request):
    return render(request, 'combination.html', locals())

# 随机分配token
def register(request):
    if request.method == "POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPass")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAddress = request.POST.get("userEmail")
        userRank = 0

        token = time.time() + random.randrange(1,100000)
        userToken = str(token)

        f = request.FILES['userImg']
        print(f)
        # userImg = os.path.join(settings.USER_ROOT, userAccount + ".png")
        userImg = userAccount + ".png"
        storageImg = os.path.join(settings.USER_ROOT, userAccount + ".png")
        # print("**************")
        # print(settings.BASE_DIR)
        # print(settings.USER_ROOT)
        # print(userImg)
        # print("**************")
        with open(storageImg, "wb") as fp:
            for data in f.chunks():
                fp.write(data)

        user = User.creatuser(userAccount, userPasswd, userName, userPhone, userAddress, userImg,
                              userRank, userToken)
        user.save()

        request.session["useraccount"] = userAccount
        request.session["username"] = userName
        request.session["token"] = userToken
        request.session["userimg"] = userImg
        request.session["userpasswd"] = userPasswd
        request.session["token"] = userToken
        request.session["userimg"] = userImg
        request.session["userphone"] = userPhone
        request.session["useraddress"] = userAddress
        request.session["userrank"] = userRank

        return redirect('/index/')

    else:
        f = RegisterForm()
        return render(request, 'pages-register.html', {"title": "注册", "form": f}, locals())


# 退出登录

def quit(request):
    logout(request)
    return redirect('/index/')


# 检测账号是否重复
def checkuserid(request):
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount = userid)
        # 有了，不能注册
        # return JsonResponse({"该账号已经被注册", "error"})
        return JsonResponse({"data":"该账号已经被注册", "status":"error"})
    except User.DoesNotExist as e:
        # return JsonResponse({"该账号可以注册", "success"})
        return JsonResponse({"data": "该账号可以注册", "status": "success"})

def login(request):
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            #信息格式没问题，验证账号和密码的正确性
            print("**********************")
            nameid = f.cleaned_data["username"]
            pswd = f.cleaned_data["passwd"]
            try:
                user = User.objects.get(userAccount = nameid)
                if user.userPasswd != pswd:
            #         c
                    return redirect("/login/")
            except User.DoesNotExist as e:
            #     c
                return redirect("/login/")

            # 登录成功
            token = time.time() + random.randrange(1, 100000)
            user.userToken = str(token)
            user.save()
            request.session["useraccount"] = user.userAccount
            request.session["username"] = user.userName
            request.session["token"] = user.userToken
            request.session["userimg"] = user.userImg
            request.session["userpasswd"] = user.userPasswd
            request.session["token"] = user.userToken
            request.session["userimg"] = user.userImg
            request.session["userphone"] = user.userPhone
            request.session["useraddress"] = user.userAddress
            request.session["userrank"] = user.userRank

            return redirect("/index/")
        else:
            return render(request, 'pages-login.html', {"title": "登录", "form": f, "error": f.errors}, locals())
    else:
        f = LoginForm()
        return render(request, 'pages-login.html', {"title": "登录", "form": f}, locals())


def forget(request):
    return render(request, 'pages-recoverpw.html', locals())


def center(request):
    username = request.session.get("username", "未登录")
    userimg = request.session.get("userimg", "../../static/assets/images/users/user-4.jpg")
    # return render(request, 'center.html', {"userimg": userimg, "username":username}, locals())
    return render(request, 'center.html', locals())


def person(request):
    useraccount = request.session.get("useraccount","未登录")
    username = request.session.get("username", "未登录")
    userimg = request.session.get("userimg", "../../static/assets/images/users/user-4.jpg")
    useraddress= request.session.get("useraddress", "未设置")
    userphone = request.session.get("userphone", "未设置")
    userpasswd = request.session.get("userpasswd", "未设置")
    return render(request, 'person.html', {"useraccount": useraccount, "username": username, "userimg": userimg, "useraddress": useraddress,
                                           "userphone": userphone, "userpasswd": userpasswd}, locals())

def detail(request):
    with open('static/strategy_data/Follow_Loser.csv', 'r') as f:
        reader = csv.DictReader(f)
        follow_loser = [dict(row) for row in reader]
    with open('static/strategy_data/Follow_Winner.csv', 'r') as f:
        reader = csv.DictReader(f)
        follow_winner= [dict(row) for row in reader]
    with open('static/strategy_data/PG_Dense.csv', 'r') as f:
        reader = csv.DictReader(f)
        pg = [dict(row) for row in reader]
    with open('static/strategy_data/UCRP.csv', 'r') as f:
        reader = csv.DictReader(f)
        # ucpr = [{row['Date']:(float)(row['Pr'])} for row in reader]
        ucpr=[dict(row) for row in reader]
    with open('static/strategy_data/PG_Dense.csv', 'r') as f:
        reader = csv.DictReader(f)
        pg_change = ([dict(row) for row in reader])
        pg_now=pg_change[-1]
    return render(request,"detail.html",locals());