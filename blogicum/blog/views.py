from django.shortcuts import render
import datetime

from .models import Post, Category, Location


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lt=datetime.datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[0:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = 0
    for post_2 in posts:
        if post_2['id'] == id:
            post = post_2
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'posts': posts,
               'category_slug': category_slug}
    return render(request, template, context)
