from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from posts.forms import PostForm
from posts.models import Post


def index_view(request):
    return render(request, 'posts/index.html', {'posts': Post.objects.all().order_by('-publish_date')})


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
    related_posts = post.get_related_posts()
    print(related_posts, len(related_posts))
    return render(request, 'posts/detail.html', {'post': post, 'related_posts': related_posts})


@login_required
def post_view(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.instance.author = request.user
            post = form.save()
            return redirect(reverse('posts:detail', args=[post.id]))

    else:
        form = PostForm()

    return render(request, 'posts/post.html', {'form': form})
