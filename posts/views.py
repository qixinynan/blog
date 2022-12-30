from django.shortcuts import render, get_object_or_404

from posts.models import Post


def index_view(request):
    return render(request, 'posts/index.html', {'posts': Post.objects.all()})


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})
