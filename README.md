# search_engine_demo
A demo for SAST Summer Training

## 规划列表

- [x] 爬虫部分
  - [x] 课程数据爬取
  - [x] 合适格式存入数据库
- [ ] 网站部分
  - [x] 前端
    - [x] 登录/注册界面
      - [x] 用户名和密码 - POST
    - [x] 网站美化
      - [x] 搜索页面
        - [ ] 顶部导航栏 Bootsrap
          - [ ] 页面切换皮肤
          - [x] 未登录时，显示登录入口；登录以后显示头像 - Gravater
        - [x] 搜索框
          - [x] 水平居中
          - [x] 上面有一个科协的logo
        - [x] 搜索
          - [x] 使用回车来发送请求 - 包裹在`<form>`元素中
          - [x] 用flex/margin-top实现竖直居中
        - [ ] 在搜索之前要先登录
          - [ ] 邮箱验证
      - [ ] 搜索结果页面
        - [x] 顶部导航栏
        - [x] 搜索框
        - [x] 搜索结果
        - [x] 分页功能
        - [x] 关键词高亮
      - [x] 详情界面
        - [x] 标题
        - [x] 内容 - 空白自动过滤，自动去空格，去除教学日历
      - [x] 配色方案：马卡龙
  - [ ] 后端
    - [x] 将爬虫数据导入sqlite3
    - [ ] 生成网站访问 log 文件
    - [ ] 认证
      - [x] 处理登录请求、注册请求
      - [x] 登录页面、注册视图页面的返回
      - [ ] 限制用户访问频率
      - [ ] 邮箱认证
    - [x] 搜索 - query string
      - [x] 用时统计、总数显示
      - [x] 分页功能
      - [ ] 按关键词出现次数排序
      - [ ] 分词制作倒排索引
      - [ ] 针对用户做搜索历史记录
      - [x] 历史热门
    - [x] 详情页面
    

## 配置教程

```bash
# Set up at Python 3.8.3, Django 3.0.3
git clone https://github.com/prnake/search_engine_demo.git
cd search_engine_demo
pip install -r requirements.txt
cd mysite
vi mysite/.env
```

```yaml
#create .env file at /path/to/mysite/mysite
DEBUG=off
SECRET_KEY='your_secret_key'
ADMIN_EMAIL='admin@example.com i@example.com'

```

Run Django:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000 --insecure
```

Sign up at  yourwebsite/signup using the email in `ADMIN_EMAIL`, then visit yourwebsite/scrapy, type in the url and cookie of course-choose website, then just wait until everything is down.
