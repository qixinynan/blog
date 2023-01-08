import random
import re
from functools import reduce

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Q
from django.db.models.signals import pre_save
from django.utils.text import Truncator


class PostManager(models.Manager):
    def total_views(self):
        return self.aggregate(total_views=Sum('views'))['total_views']


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='文章标题')
    description = models.TextField(max_length=120, blank=True, verbose_name='文章描述', help_text='留空则自动截取文章前120个字符')
    keywords = models.CharField(max_length=255, verbose_name='关键字', help_text='多个关键词使用","分割')
    content = RichTextUploadingField(verbose_name="内容")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='发布日期')

    objects = PostManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def get_related_posts(self):
        required_count = 10
        keywords = [keyword.strip() for keyword in self.keywords.split(',')]

        query = reduce(lambda x, y: x | y, [Q(keywords__contains=keyword) for keyword in keywords])
        related_posts = Post.objects.filter(query).exclude(id=self.id)

        if related_posts.count() < required_count:
            post_ids = Post.objects.values_list('id', flat=True)
            post_ids = post_ids.exclude(id__in=related_posts.values_list('id', flat=True))
            post_ids = post_ids.exclude(id=self.id)
            post_ids = sorted(post_ids)
            if len(post_ids) < required_count:
                random_posts = Post.objects.filter(id__in=post_ids)
            else:
                random_posts = Post.objects.filter(id__in=random.sample(post_ids, required_count))
            related_posts = list(related_posts) + list(random_posts)

        return related_posts[:required_count]


def update_description(sender, instance, **kwargs):
    if not instance.description:
        stripped_html = re.sub(r'<[^<]+?>', '', instance.content)
        instance.description = Truncator(stripped_html).chars(120)


pre_save.connect(update_description, sender=Post)
