# 基于Django的博客设计

Django版本： 4.1.0

# 运行

```shell script
conda  install django
django-admin startpeoject blog_by_django
python manage.py runserver
```

# 创建django应用

```shell script
python manage.py startapp blog
```

## blog应用目录介绍

- view.py 视图处理的地方
- model.py 定义应用模型的地方
- admin.py 定义Admin模块管理对象的地方
- apps.py 声名应用的地方
- test.py 编写测试用例的文件


## 模型层简介

模型层是Django的核心，它定义了数据库的表结构，以及数据表的字段。
视图层<=>模型层<=>数据库

### 模型层配置
```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 使用的数据库启动
        'NAME': BASE_DIR / 'db.sqlite3', # 数据库文件名
    }
}
```
### 创建微博客文章模型
```python
class Article(models.Model):
    article_id  = models.AutoField(primary_key=True) # 自增主键
    article_title = models.TextField()  # 文章题目
    article_abstract = models.TextField() # 文章摘要
    article_content = models.TextField()  # 文章内容
    article_pub_time = models.DateTimeField(auto_now_add=True)  # 文章发布时间

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
