from django.shortcuts import render, get_object_or_404
import datetime
from django.db.models import Q

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
    post = get_object_or_404(
        Post,
        pub_date__lt=datetime.datetime.now(),
        is_published=True,
        category__is_published=True,
        id=id

    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    post_list = Post.objects.filter(
        category=category,
        pub_date__lt=datetime.datetime.now(),
        is_published=True
    )
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
