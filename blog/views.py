from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

def article_content(request):
    article = Article.objects.all()[0]
    title = article.article_title
    abstract = article.article_abstract
    content = article.article_content
    id = article.article_id
    pub_time = article.article_pub_time
    return_str = "title: %s <br> abstract: %s <br> content: %s <br> id: %s <br> pub_time: %s" % (title, abstract, content, id,pub_time)
    return HttpResponse(return_str)