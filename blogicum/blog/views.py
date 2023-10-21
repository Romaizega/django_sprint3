import datetime
from django.shortcuts import render, get_object_or_404

from blog.models import Category, Post

MAX_POST_PAGE = 5


def base_query():
    return Post.objects.select_related(
        'location', 'author', 'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.datetime.now())


def index(request):
    post_list = base_query()[:MAX_POST_PAGE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(base_query(), id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    post_list = base_query().filter(
        category=category)
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list}
    )
