from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from tinymce.models import HTMLField


class PostManager(models.Manager):
    def total_views(self):
        return self.aggregate(total_views=Sum('views'))['total_views']


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='文章标题')
    description = models.TextField(blank=True, verbose_name='文章描述')
    keywords = models.CharField(max_length=255, verbose_name='关键字', help_text='多个关键词使用","分割')
    content = HTMLField(verbose_name="内容")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='发布日期')

    objects = PostManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
