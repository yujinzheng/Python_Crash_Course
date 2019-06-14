"""pizzas的url"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 披萨的主页
    url(r'^$', views.index, name='index'),

    # 显示所有的披萨
    url(r'^name/$', views.names, name='names'),

    # 显示特定披萨的详细页面
    url(r'^name/(?P<name_id>\d+)/$', views.name, name='name')
]
