from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """定义博客文章的模型"""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title

class Content(models.Model):
    """博客的内容"""
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."