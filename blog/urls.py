from django.urls import path
import blog.views

urlpatterns = [
    # path("hello_world/", blog.views.hello_world),
    # path("content/", blog.views.article_content),
    # path("index/<int:page>/", blog.views.get_index_page),
    path("index/", blog.views.get_index_page),
    path("detail/<int:article_id>/", blog.views.get_detail_page),
]
