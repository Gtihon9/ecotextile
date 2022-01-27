from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

MAX_POSTS_IN_PAGE = 3

def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, MAX_POSTS_IN_PAGE)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'news/post/list.html',
                  {'page': page,
                   'posts': posts})

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request,'news/post/detail.html', {'post': post})
