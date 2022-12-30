from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='文章标题')
    description = models.TextField(blank=True, verbose_name='文章描述')
    keywords = models.CharField(max_length=255, verbose_name='关键字', help_text='多个关键词使用","分割')
    content = RichTextField(verbose_name='内容')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
