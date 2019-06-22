"""为应用程序blogs定义URL模式"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页面
    url(r'^$', views.index, name='index'),
    # 所有博客的页面
    url(r'^blogpost/$', views.blogposts, name='blogposts'),
    # 某个博客的页面
    url(r'^blogpost/(?P<blogpost_id>\d+)$', views.blogpost, name='blogpost'),
    # 新建博客
    url(r'^new_blogpost/$', views.new_blogpost, name='new_blogpost'),
    # 编辑博客
    url(r'^edit_content/(?P<content_id>\d+)$', views.edit_content, name='edit_content'),
]
