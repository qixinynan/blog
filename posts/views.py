from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from posts.models import Post


def index_view(request):
    return render(request, 'posts/index.html', {'posts': Post.objects.all()})


def search_view(request):
    if 'query' not in request.GET:
        return redirect(reverse('posts:index'))

    query = request.GET.get('query')
    keywords = query.split()
    posts = Post.objects.all()

    for keyword in keywords:
        posts = posts.filter(
            Q(title__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(keywords__icontains=keyword))

    return render(request, 'posts/search.html', {'posts': posts, 'query': query})


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if 'viewed' not in request.session:
        request.session['viewed'] = f'{post_id}'
        post.views += 1
        post.save()
    else:
        viewed = request.session['viewed'].split(',')
        if str(post_id) not in viewed:
            viewed.append(str(post_id))
            request.session['viewed'] = ','.join(viewed)
            post.views += 1
            post.save()
    print(f'viewed session: {request.session["viewed"]}')
    return render(request, 'posts/detail.html', {'post': post})
