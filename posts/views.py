import markdown
from django.shortcuts import render, get_object_or_404

from posts.models import Post


def index_view(request):
    return render(request, 'posts/index.html', {'posts': Post.objects.all()})


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # TODO 缓存
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    body = md.convert(post.content)
    response = render(request, 'posts/detail.html', {'post': post, 'body': body})
    if 'viewed' not in request.COOKIES:
        response.set_cookie('viewed', f'{post_id}', max_age=60 * 60 * 24 * 365)
        post.views += 1
        post.save()
    else:
        viewed = request.COOKIES['viewed'].split(',')
        if str(post_id) not in viewed:
            viewed.append(str(post_id))
            response.set_cookie('viewed', ','.join(viewed), max_age=60 * 60 * 24 * 365)
            post.views += 1
            post.save()

    return response
