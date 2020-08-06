from django.shortcuts import render,redirect,reverse
from datetime import datetime
from . import forms
from . import models

# Create your views here.

def search_home(request):
    params = {
        'title': '课程搜索系统',
        'description':''
    }
    return render(request,'search/index.html', locals())

def search_list(request):
    params = {
        'title': '课程搜索系统',
        'description': ''
    }
    searchbox = True
    return render(request,'search/result.html', locals())


def show_content(request):
    print()

def login(request):
    if reverse('login'):
        if request.session.get('is_login', None):  # 不允许重复登录
            return redirect('/')
        if request.method == "POST":
            login_form = forms.UserForm(request.POST)
            message = "请检查填写的内容！"
            if login_form.is_valid():
                email = request.POST.get("email")
                password = request.POST.get("password")
                try:
                    user = models.User.objects.get(email=email)
                except:
                    message = "用户不存在！"
                    return render(request, 'search/login.html', locals())
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_email'] = user.email
                    return redirect('/')
                else:
                    message = "密码不正确！"
                    return render(request, 'search/login.html', locals())
            else:
                return render(request, 'search/login.html', locals())
        login_form = forms.UserForm()
        return render(request, 'search/login.html',locals())

def signup(request):
    if reverse('signup'):
        if request.session.get("is_login", None):
            return redirect('/')
        if request.method == "POST":
            register_form = forms.RegisterForm(request.POST)
            message = "请检查填写的内容！"
            if register_form.is_valid():
                email = register_form.cleaned_data.get('email')
                password = register_form.cleaned_data.get('password')
                password_repeat = register_form.cleaned_data.get('password_repeat')
                if password != password_repeat:
                    message = '两次输入的密码不同！'
                    return render(request, 'search/signup.html', locals())
                else:
                    same_email_user = models.User.objects.filter(email=email)
                    if same_email_user:
                        message = '该邮箱已经被注册了！'
                        return render(request, 'search/signup.html', locals())
                    new_user = models.User()
                    new_user.email = email
                    new_user.password = password
                    new_user.save()
                    request.session['is_login'] = True
                    request.session['user_email'] = email
                    return redirect('/')
            else:
                return render(request, 'search/signup.html', locals())
        register_form = forms.RegisterForm()
        return render(request, 'search/signup.html', locals())


def logout(request):
    if reverse('logout') and request.session.get("is_login", None):
        request.session.flush()
    return redirect("/login/")