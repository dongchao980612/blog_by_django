from django.core.paginator import Paginator
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
    return_str = "title: %s <br> abstract: %s <br> content: %s <br> id: %s <br> pub_time: %s" % (
        title, abstract, content, id, pub_time)
    return HttpResponse(return_str)


def get_index_page(request):
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)

    all_articles = Article.objects.all().order_by("article_id")
    paginator = Paginator(all_articles, 4)
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    top5_list = Article.objects.all().order_by("article_pub_time")[:5]
    return render(request, 'blog/index.html', {
        "articles_list": page_article_list,
        "page_num": range(1, page_num + 1),
        "cur_page": page,
        "previous_page": previous_page,
        "next_page": next_page, 
        "top5_list": top5_list
    })


def get_detail_page(request, article_id):
    try:
        current_article = Article.objects.get(article_id=article_id)
    except Article.DoesNotExist:
        return render(request, 'blog/error.html', {"message": "文章不存在"})
    
    # 获取上一篇文章（按 article_id 排序）
    previous_article = Article.objects.filter(article_id__lt=article_id).order_by('article_id').first()

    # 获取下一篇文章（按 article_id 排序）
    next_article = Article.objects.filter(article_id__gt=article_id).order_by('article_id').first()

    section_list = current_article.article_content.split('\n')
    return render(request, 'blog/detail.html', {
        "current_article": current_article,
        "section_list": section_list,
        "previous_article": previous_article,
        "next_article": next_article
    })
