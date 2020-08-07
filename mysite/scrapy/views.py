from django.shortcuts import render
from .models import Post,Teacher
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from .forms import LogForm
from . import models
from django.db.models import Max

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re
from lxml import etree

# Create your views here.

def class_spider(request):
    if not request.session.get('is_login') or request.session.get('user_email') not in ["admin","prnake@gmail.com"]:  # 不允许重复登录
        return redirect('/')
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            cookie = form.cleaned_data.get('cookie')
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')
            spider = ThuSpider(url,cookie)
            end = min(end,spider.get_max_page())
            try:
                spider.parse_page(start,end)
            except:
                print("Error!")
            return redirect('/scrapy/')
    else:
        context = {}
        context['form'] = LogForm()
        return render(request, 'scrapy/index.html', context)

class ThuSpider(object):
    def __init__(self, url, cookie):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random, "Cookie": cookie}
        self.data = list()
        self.url = url

    def get_max_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200 and '网瑞达' not in response.text:
            soup = BeautifulSoup(response.text, 'html.parser')
            a = soup.select('p[class="yeM yahei"]')
            max_page = int(re.search(r'共 (\d+) 页',a[0].get_text()).group(1))
            return max_page
        else:
            print("Cookie已失效")
            return None
    def parse_page(self,start=1,end=10):
        #end = self.get_max_page()+1
        data = {'m': 'kkxxSearch','page': '2','token': '7348aedd571905c8cb54932742acf6f0','p_sort.asc1': 'true','p_sort.asc2': 'true','p_xnxq': 2020-2021-1,'pathContent': '%D2%BB%BC%B6%BF%CE%BF%AA%BF%CE%D0%C5%CF%A2','goPageNumber': '1'}
        for count in range(start,end):
            print("正在处理第%d页" % count)
            data['page'] = count
            response = requests.post(self.url, data=data,headers=self.headers)
            if response.status_code == 200 and '网瑞达' not in response.text:
                soup = BeautifulSoup(response.text, 'html.parser')
                a = soup.find_all("tr",class_="trr2")
                for item in a:
                    b = [""] * 20
                    detail = dict()
                    row = item.select('td')
                    for i,word in enumerate(row):
                        b[i] = re.sub(r"\s","",word.get_text())
                    try:
                        detail['class_url'] = 'https://webvpn.tsinghua.edu.cn/http/77726476706e69737468656265737421eaff4b8b3f3b2653770bc7b88b5c2d320506b1aec738590a49ba/' + row[3].find('a')['href']
                    except:
                        detail['class_url'] = ''
                    detail['department'] = b[0]
                    detail['class_id'] = b[1]
                    detail['class_alter_id'] = b[2]
                    detail['title'] = b[3]
                    detail['study_credit'] = b[4]
                    detail['teacher'] = b[5]
                    try:
                        detail['teacher_url'] = 'https://webvpn.tsinghua.edu.cn/http/77726476706e69737468656265737421eaff4b8b3f3b2653770bc7b88b5c2d320506b1aec738590a49ba/' + row[5].find('a')['href']
                    except:
                        detail['teacher_url'] = ''
                    detail['a12'] = b[6]
                    detail['a13'] = b[7]
                    detail['a14'] = b[8]
                    detail['a15'] = b[9]
                    detail['a16'] = b[10]
                    detail['a17'] = b[11]
                    detail['a18'] = b[12]
                    detail['a19'] = b[13]
                    detail['a20'] = b[14]
                    detail['a21'] = b[15]
                    detail['a22'] = b[16]
                    if detail['class_url']:
                        class_r = requests.get(detail['class_url'], headers=self.headers)
                        if response.status_code == 200 and '网瑞达' not in response.text:
                            html = etree.HTML(class_r.text)
                            html = etree.tostring(html)
                            class_soup = BeautifulSoup(html, 'html.parser')
                            c = class_soup.select('table.table-striped > tr > td')
                            d = [""] * 40
                            for i, item in enumerate(c):
                                if i in [10, 12, 14]:
                                    d[i] = item.get_text().strip() if re.sub(r"\s", "", item.get_text()) else ""
                                else:
                                    d[i] = re.sub(r"\s", "", item.get_text())
                            detail['body'] = d[0]
                            detail['study_hour'] = d[6]
                            detail['introduction'] = d[10]
                            detail['en_introduction'] = d[12]
                            detail['a1'] = d[14]
                            detail['a2'] = d[16]
                            detail['a3'] = d[18]
                            detail['a4'] = d[20]
                            detail['a5'] = d[22]
                            detail['a6'] = d[24]
                            detail['a7'] = d[26]
                            detail['a8'] = d[28]
                            detail['a9'] = d[30]
                            detail['a10'] = d[32]
                            detail['a11'] = d[34]
                        else:
                            print("Cookie已失效")
                            return None
                    else:
                        detail['body'] = ''
                        detail['study_hour'] = ''
                        detail['introduction'] = ''
                        detail['en_introduction'] = ''
                        detail['a1'] = ''
                        detail['a2'] = ''
                        detail['a3'] = ''
                        detail['a4'] = ''
                        detail['a5'] = ''
                        detail['a6'] = ''
                        detail['a7'] = ''
                        detail['a8'] = ''
                        detail['a9'] = ''
                        detail['a10'] = ''
                        detail['a11'] = ''
                    if detail['teacher_url']:
                        teacher_r = requests.get(detail['teacher_url'], headers=self.headers)
                        if response.status_code == 200 and '网瑞达' not in response.text:
                            class_soup = BeautifulSoup(teacher_r.text, 'html.parser')
                            c = class_soup.select('table.table-striped > tbody > tr > td')
                            d = [""] * 40
                            for i, item in enumerate(c):
                                if i in [5,17]:
                                    d[i] = item.get_text().strip() if re.sub(r"\s", "", item.get_text()) else ""
                                else:
                                    d[i] = re.sub(r"\s", "", item.get_text())
                            detail['teacher_id'] = d[1]
                            detail['teacher_name'] = d[5]
                            detail['teacher_sex'] = d[7]
                            detail['teacher_a1'] = d[9]
                            detail['teacher_a2'] = d[11]
                            detail['teacher_a3'] = d[13]
                            detail['teacher_a4'] = d[15]
                            detail['teacher_a5'] = d[17]
                            detail['teacher_a6'] = d[19]
                            detail['teacher_a7'] = d[21]
                        else:
                            print("Cookie已失效")
                            return None
                    else:
                        detail['teacher_id'] = ''
                        detail['teacher_name'] = ''
                        detail['teacher_sex'] = ''
                        detail['teacher_a1'] = ''
                        detail['teacher_a2'] = ''
                        detail['teacher_a3'] = ''
                        detail['teacher_a4'] = ''
                        detail['teacher_a5'] = ''
                        detail['teacher_a6'] = ''
                        detail['teacher_a7'] = ''
                    self.data.append(detail)
                    print(detail)
            else:
                print("Cookie已失效")
                return None
            print("第%d页处理完成" % count)
            self.save_data_to_model()
    def save_data_to_model(self):
        count = models.Post.objects.order_by('-id')[0].id + 1
        for item in self.data:
            try:
                models.Post.objects.get(url=item['url'],class_id=item['class_id'],class_alter_id=item['class_alter_id'])
            except:
                new_post = Post()
                new_post.id = count
                count += 1
                new_post.url = item['class_url']
                new_post.title = item['title']
                new_post.body = item['body']
                new_post.department = item['department']
                new_post.teacher = item['teacher']
                new_post.teacher_id = item['teacher_id']
                new_post.class_id = item['class_id']
                new_post.class_alter_id = item['class_alter_id']
                new_post.study_credit = item['study_credit']
                new_post.study_hour = item['study_hour']
                new_post.introduction = item['introduction']
                new_post.en_introduction = item['en_introduction']
                new_post.a1 = item['a1']
                new_post.a2 = item['a2']
                new_post.a3 = item['a3']
                new_post.a4 = item['a4']
                new_post.a5 = item['a5']
                new_post.a6 = item['a6']
                new_post.a7 = item['a7']
                new_post.a8 = item['a8']
                new_post.a9 = item['a9']
                new_post.a10 = item['a10']
                new_post.a11 = item['a11']
                new_post.a12 = item['a12']
                new_post.a13 = item['a13']
                new_post.a14 = item['a14']
                new_post.a15 = item['a15']
                new_post.a16 = item['a16']
                new_post.a17 = item['a17']
                new_post.a18 = item['a18']
                new_post.a19 = item['a19']
                new_post.a20 = item['a20']
                new_post.a21 = item['a21']
                new_post.a22 = item['a22']
                new_post.save()
            try:
                models.Teacher.objects.get(url=item['teacher_url'],id=item['teacher_id'],name=item['teacher_name'])
            except:
                new_teacher = Teacher()
                new_teacher.id = item['teacher_id']
                new_teacher.name = item['teacher_name']
                new_teacher.url = item['teacher_url']
                new_teacher.sex = item['teacher_sex']
                new_teacher.a1 = item['teacher_a1']
                new_teacher.a2 = item['teacher_a2']
                new_teacher.a3 = item['teacher_a3']
                new_teacher.a4 = item['teacher_a4']
                new_teacher.a5 = item['teacher_a5']
                new_teacher.a6 = item['teacher_a6']
                new_teacher.a7 = item['teacher_a7']
                new_teacher.save()
        self.data.clear()
