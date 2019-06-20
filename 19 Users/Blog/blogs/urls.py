"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
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
