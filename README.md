# 基于Django的博客设计

Django版本： 4.1.0

# 运行

```shell script
conda  install django
django-admin startpeoject blog_by_django
python manage.py runserver
```

# 开发流程
## Django应用
## 创建django应用

```shell script
python manage.py startapp blog
```

### blog应用目录介绍

- view.py 视图处理的地方
- model.py 定义应用模型的地方
- admin.py 定义Admin模块管理对象的地方
- apps.py 声名应用的地方
- test.py 编写测试用例的文件

### 添加应用

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # myapp
    "blog.apps.BlogConfig"
]
```
### 配置子路由
```python
# blog/urls.py
urlpatterns = [
    path("hello_world/", blog.views.hello_world),
    path("content/", blog.views.article_content),
]
```
### 配置主路由
```python
# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))  # 添加blog应用
]
```
## 模型层简介

模型层是Django的核心，它定义了数据库的表结构，以及数据表的字段。
视图层<=>模型层<=>数据库

### 模型层配置
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 使用的数据库启动
        'NAME': BASE_DIR / 'db.sqlite3', # 数据库文件名
    }
}
```
### 创建微博客文章模型
```python
# blog/models.py
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)  # 自增主键
    article_title = models.TextField()  # 文章题目
    article_abstract = models.TextField()  # 文章摘要
    article_content = models.TextField()  # 文章内容
    article_pub_time = models.DateTimeField(auto_now_add=True)  # 文章发布时间

    def __str__(self):
        return self.article_title

```
### 迁移数据库
```shell script
python manage.py makemigrations # 创建迁移文件
python manage.py migrate # 迁移数据库
```
### django-shell
```shell script
python manage.py shell
```
##  初识Django的admin模块
Django的admin模块是Django的核心模块，它提供了一套完整的后台管理界面，用于管理数据库中的数据。
### 创建管理员
```shell script
python manage.py createsuperuser
```
### 注册管理员
```shell script
# blog/admin.py
from .models import Article
admin.site.register(Article)
```
### 修改中文
```python
# settings.py
LANGUAGE_CODE = 'zh-hans'
```
