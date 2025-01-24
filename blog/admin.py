from django.contrib import admin
from .models import Article


# 自定义ArticleAdmin类
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'article_title', 'article_pub_time')
    search_fields = ('article_title',)
    list_filter = ('article_pub_time',)


# 注册Article模型到admin站点，并使用自定义的ArticleAdmin
admin.site.register(Article,ArticleAdmin)
