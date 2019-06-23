# Django学习笔记

## 创建Django项目的过程

1. 创建项目

        django-admin.exe startproject projectname

2. 创建数据库

        python manage.py migrate

3. 创建应用程序

        python manage.py startapp appname

4. 在models.py中为应用程序定义模型
5. 在settings.py中激活模型，激活的名字就是appname
6. 创建新的数据库

        python manage.py makemigrations appname

7. 将新的数据库合入到数据库中

        python manage.py migrate

8. 创建超级用户

        python manage.py createsuperuser

9. 向管理网站注册模型

        admin.site.register(modelname)

小知识：

1. 如何定义存储少量数据的字符？

使用models.CharField(max_length=lenght)来定义

2. 如何在添加数据的时候记录日期和时间的数据？

使用models.DateField(auto_now_add=True)来定义

3. 如何定义文本实例？

使用models.TextField()来定义

4. 如何关联外键？

使用models.ForeignKey(外键, on_delete=models.CASCADE)来关联

## 创建网页

Django创建网页的三阶段：定义URL、编写视图和编写模版。

URL模式描述URL如何设计，让Django知道如何将浏览器请求和网站URL匹配；每个URL都会映射到特定的视图——视图函数获取并处理网页所需的数据；视图函数通常调用一个模版，模版生成浏览器能够理解的网页。

1. 在项目的url.py文件中注册url信息，namespace是为了将url与项目中其他的url分开

        url(r'', include('appname.urls', namespace='appname'))

2. 在app的url.py中注册url信息，在这里可以将url信息与视图绑定

	    url(r'^$', views.index, name='index')

3. 在views.py中构造与url绑定的视图信息，可以返回模板

        def index(request):
            """学习笔记的主页"""
            return render(request, 'appname/index.html')

4. 在app目录下新建templates/appname文件夹，在里面放入index.html文件，就能够通过url访问到主页了

## 用户账户

可以使用HttpResponseRedirect和reverse来帮助用户在完成操作后重定向到指定页面

        return HttpResponseRedirect(reverse('learning_logs:index')) # 在操作完成后让用户返回到index页面，即重定向

POST提交表单，GET获取表单，通过form.is_valid()能够判断表单是否有效

在没有提交表单（即没有检测到POST）时，可以返回空表单，空表单不会对我们的填写造成影响

如果想要通过用户账户来对页面进行管理，需要引入login_required

        from django.contrib.auth.decorators import login_required
        @login_required # 添加修饰可以让下面的函数对当前用户进行校验

需要在settings中指定用户校验跳转的页面：

        LOGIN_URL = '/users/login/'

在model中，可以引入User，将数据与User连接起来，就能够实现分用户的数据管理

        from django.contrib.auth.models import User
		owner = models.ForeignKey(User)