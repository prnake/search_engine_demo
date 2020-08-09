from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    url = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=50,verbose_name='课程名',blank=True)
    body = models.TextField(default='什么信息都没有哦～',verbose_name='全文',blank=True)
    department = models.TextField(default='未知',verbose_name='开课院系',blank=True)
    teacher = models.TextField(default='未知',verbose_name='主讲教师',blank=True)
    teacher_id = models.CharField(max_length=20,default='0',verbose_name='教师号',blank=True)
    class_id = models.CharField(max_length=20,verbose_name='课程号',blank=True)
    class_alter_id = models.CharField(max_length=20, verbose_name='课序号', blank=True)
    study_credit = models.CharField(max_length=20,default='0', verbose_name='学分',blank=True)
    study_hour = models.CharField(max_length=20,default=0,verbose_name='总学时',blank=True)
    introduction = models.TextField(default='什么信息都没有哦～',verbose_name='课程内容简介',blank=True)
    en_introduction = models.TextField(verbose_name='Course Description',blank=True)
    a1 = models.TextField(verbose_name='进度安排',blank=True)
    a2 = models.TextField(verbose_name='考核方式',blank=True)
    a3 = models.TextField(verbose_name='教材及参考书',blank=True)
    a4 = models.TextField(verbose_name='主教材',blank=True)
    a5 = models.TextField(verbose_name='参考书',blank=True)
    a6 = models.TextField(verbose_name='合开教师',blank=True)
    a7 = models.TextField(verbose_name='选课指导',blank=True)
    a8 = models.TextField(verbose_name='先修要求',blank=True)
    a9 = models.TextField(verbose_name='教师教学特色',blank=True)
    a10 = models.TextField(verbose_name='Office Hour',blank=True)
    a11 = models.TextField(verbose_name='成绩评定标准',blank=True)
    a12 = models.TextField(verbose_name='本科生课容量', blank=True)
    a13 = models.TextField(verbose_name='研究生课容量', blank=True)
    a14 = models.TextField(verbose_name='上课时间', blank=True)
    a15 = models.TextField(verbose_name='选课文字说明', blank=True)
    a16 = models.TextField(verbose_name='课程特色', blank=True)
    a17 = models.TextField(verbose_name='年级', blank=True)
    a18 = models.TextField(verbose_name='是否二级选课', blank=True)
    a19 = models.TextField(verbose_name='实验信息', blank=True)
    a20 = models.TextField(verbose_name='重修是否占容量', blank=True)
    a21 = models.TextField(verbose_name='是否选课时限制', blank=True)
    a22 = models.TextField(verbose_name='本科文化素质课组', blank=True)
    top_50 = models.BooleanField(verbose_name='学生评教TOP50%',default=False)
    recommend = models.FloatField(verbose_name='选课学生推荐度',default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = "课程信息"

class Teacher(models.Model):
    id = models.CharField(primary_key=True,max_length=20,verbose_name='教师号')
    url = models.CharField(max_length=50,blank=True)
    name = models.CharField(max_length=10, verbose_name='姓名',blank=True)
    sex = models.CharField(max_length=10, verbose_name='性别',blank=True)
    a1 = models.TextField(verbose_name='职称', blank=True)
    a2 = models.TextField(verbose_name='单位', blank=True)
    a3 = models.TextField(verbose_name='电话', blank=True)
    a4 = models.TextField(verbose_name='E-Mail', blank=True)
    a5 = models.TextField(verbose_name='个人简介', blank=True)
    a6 = models.TextField(verbose_name='主要研究方向', blank=True)
    a7 = models.TextField(verbose_name='研究方向简介', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = "教师信息"




