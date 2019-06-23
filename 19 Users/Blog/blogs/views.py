from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .models import BlogPost, Content
from .forms import BlogPostForm, ContentForm
from django.contrib.auth.decorators import login_required

def index(request):
    """主页视图"""
    return render(request, 'blogs/index.html')

@login_required
def blogposts(request):
    """显示所有博客"""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts' : blogposts}
    return render(request, 'blogs/blogposts.html', context)

@login_required
def blogpost(request, blogpost_id):
    """显示单个主题及其内容"""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    check_blog_owner(request, blogpost)
    contents = blogpost.content_set.all()
    if len(contents) == 0:
        content = Content.objects.create()
    else:
        for temp in contents:
            content = Content.objects.get(id=temp.id)
    context = {'blogpost' : blogpost, 'content' : content}
    return render(request, 'blogs/blogpost.html', context)

@login_required
def new_blogpost(request):
    """新建博客的页面"""
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = BlogPostForm()
    else:
        # POST提交数据，对数据进行处理
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogposts'))

    context = {'form' : form}
    return render(request, 'blogs/new_blogpost.html', context)

@login_required
def edit_content(request, content_id):
    """编辑文本的界面"""
    content = Content.objects.get(id=content_id)
    blogpost = content.blogpost
    check_blog_owner(request, blogpost)

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = ContentForm(instance=content)
    else:
        # POST 提交的数据，对数据进行处理
        form = ContentForm(instance=content, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogpost', args=[blogpost.id]))

    context = {'blogpost' : blogpost, 'content' : content, 'form' : form}
    return render(request, 'blogs/edit_content.html', context)

def check_blog_owner(request, blogpost):
    """检查当前博客是否属于当前用户"""
    if blogpost.owner != request.user:
        raise Http404