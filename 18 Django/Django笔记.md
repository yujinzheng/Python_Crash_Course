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

