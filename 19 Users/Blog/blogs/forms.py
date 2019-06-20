from django import forms

from .models import BlogPost, Content

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title']
        labels = {'title' : ''}

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = {'text'}
        labels = {'text' : ''}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}