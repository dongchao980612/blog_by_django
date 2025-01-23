from django.db import models

# Create your models here.
class Article(models.Model):
    article_id  = models.AutoField(primary_key=True) # 自增主键
    article_title = models.TextField()  # 文章题目
    article_abstract = models.TextField() # 文章摘要
    article_content = models.TextField()  # 文章内容
    article_pub_time = models.DateTimeField(auto_now_add=True)  # 文章发布时间
 