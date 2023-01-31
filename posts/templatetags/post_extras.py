from django import template
from django.contrib.auth.models import User

from posts.models import Post

register = template.Library()


@register.simple_tag
def get_latest_post(num=10):
    return Post.objects.all().order_by('-publish_date')[:num]


@register.simple_tag()
def get_most_views_post(num=10):
    return Post.objects.all().order_by('-views')[:num]


@register.simple_tag()
def get_posts_by_user(user: User, num=10):
    return Post.objects.filter(author_id=user.id)[:num]


@register.simple_tag()
def get_posts_count():
    return Post.objects.count()


@register.simple_tag()
def get_posts_views():
    return Post.objects.total_views()
