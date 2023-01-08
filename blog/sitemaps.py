from django.contrib.auth.models import User
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from posts.models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Post.objects.all().order_by('-publish_date')

    def lastmod(self, item: Post):
        return item.publish_date

    def location(self, item):
        return reverse('posts:detail', args=[item.id])


class UserSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return User.objects.all()

    def location(self, item):
        return reverse('users:detail', args=[item.id])


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'posts:index', 'users:login']

    def location(self, item):
        return reverse(item)
