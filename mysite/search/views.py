from django.shortcuts import render
from datetime import datetime

# Create your views here.

def search_home(request):

    params = {
        'title': '课程搜索系统',
        'description':''
    }
    return render(request,'search/index.html', params)

def search_list(request):
    params = {
        'title': '课程搜索系统',
        'description': ''
    }
    return render(request, 'search/result.html', params)


def show_content(request):
    print()

def search_login(request):
    params = {
        'title': '课程搜索系统',
        'description': ''
    }
    return render(request, 'search/login.html', params)

def search_signup(request):
    params = {
        'title': '课程搜索系统',
        'description': ''
    }
    return render(request, 'search/signup.html', params)