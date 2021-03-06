import time
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from . import forms, models
from .models import HotSpot
from scrapy.models import Post, Teacher
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.


def search_home(request):
    title = "Course Search"
    content = "Anything that can go wrong will go wrong."
    return render(request, 'search/index.html', locals())


def search_list(request):
    # if not request.session.get('is_login'):
    #    return redirect('/login')
    start_time = time.time()
    searchbox = True
    keywords = request.GET.get('q')
    message = ''
    if not keywords:
        return redirect('/')
    words = keywords.split(' ')
    post_list = Post.objects.order_by('-recommend', '-top_50')
    for word in words:
        post_list = post_list.filter(Q(body__icontains=word) | Q(teacher__icontains=word) | Q(department__icontains=word) | Q(
            a14__icontains=word) | Q(a15__icontains=word) | Q(a16__icontains=word) | Q(a17__icontains=word))
        try:
            old_word = HotSpot.objects.get(word=word)
        except:
            new_word = HotSpot()
            new_word.word = word
            new_word.count += 1
            new_word.save()
        else:
            old_word.count += 1
            old_word.save()
    limit = 10
    paginator = Paginator(post_list, limit)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        posts = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        posts = paginator.page(paginator.num_pages)  # 取最后一页的记录

    end_time = time.time()
    load_time = end_time-start_time

    title = keywords + " - Course Search"
    content = "Anything that can go wrong will go wrong."

    return render(request, 'search/result.html', locals())


def show_detail(request, post_id):
    # if not request.session.get('is_login'):
    #    return redirect('/login')
    try:
        post = Post.objects.get(id=post_id)
    except:
        return redirect('/')
    ignore_list = ['id', 'title', 'body', 'url']
    params = [[f.verbose_name, post.__dict__[f.name]]
              for f in post._meta.fields if f.name not in ignore_list and post.__dict__[f.name]]

    title = post.title
    content = post.department + " " + post.teacher

    return render(request, 'search/detail.html', locals())


def show_teacher(request, teacher_id):
    # if not request.session.get('is_login'):
    #    return redirect('/login')
    try:
        post = Teacher.objects.get(id=teacher_id)
    except:
        return redirect('/')
    ignore_list = ['url']
    params = [[f.verbose_name, post.__dict__[f.name]]
              for f in post._meta.fields if f.name not in ignore_list and post.__dict__[f.name]]

    title = post.name
    content = post.a5

    return render(request, 'search/teacher.html', locals())


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

        title = "Log in"
        content = "Anything that can go wrong will go wrong."

        return render(request, 'search/login.html', locals())


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
                password_repeat = register_form.cleaned_data.get(
                    'password_repeat')
                if len(password) > 200:
                    message = '输入的密码过长！'
                    return render(request, 'search/signup.html', locals())
                elif password != password_repeat:
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
                    if 'HTTP_X_FORWARDED_FOR' in request.META:
                        new_user.ip = request.META['HTTP_X_FORWARDED_FOR']
                    else:
                        new_user.ip = request.META['REMOTE_ADDR']
                    new_user.save()
                    request.session['is_login'] = True
                    request.session['user_email'] = email
                    return redirect('/')
            else:
                return render(request, 'search/signup.html', locals())
        register_form = forms.RegisterForm()

        title = "Sign up"
        content = "Anything that can go wrong will go wrong."

        return render(request, 'search/signup.html', locals())


def logout(request):
    if reverse('logout') and request.session.get("is_login", None):
        request.session.flush()
    return redirect("/login/")
