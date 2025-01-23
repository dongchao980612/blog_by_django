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
