from django.shortcuts import render
from .models import Post,Teacher
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from .forms import LogForm

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re

# Create your views here.

def class_spider(request):
    if request.session.get('is_login', None) or request.session.get('user_email') != "admin":  # 不允许重复登录
        return redirect('/')
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            cookie = form.cleaned_data.get('cookie')
            return redirect('/')
    else:
        return redirect('/')

class ThuSpider(object):
    def __init__(self, url, cookie):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random, "Cookie": cookie}
        self.data = list()
        self.url = url

    
