from django.shortcuts import render




def index(request):
    template = 'blog/index.html'
    rev_posts = reversed(posts)
    context = {'rev_posts': rev_posts}
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
