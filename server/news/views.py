from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Image

MAX_POSTS_IN_PAGE = 3

def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, MAX_POSTS_IN_PAGE)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/post/list.html', {'page': page, 'posts': posts})

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    images = Image.objects.filter(attached_to=post)
    return render(request,'news/post/detail.html', {'post': post, 'images': images})
