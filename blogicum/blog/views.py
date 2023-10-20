import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
from django.http import Http404


def index(request):
    post_list = (
        Post.objects.select_related(
            'location', 'author', 'category'
        ).filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=datetime.datetime.now()
        ).order_by('-pub_date')[:5]
    )
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related(
            'location', 'author', 'category'
        ).filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=datetime.datetime.now()
        ),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.all(),
        is_published=True,
        slug=category_slug
    )
    post_list = (
        Post.objects.select_related(
            'location', 'author', 'category'
        ).filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=datetime.datetime.now(),
            category=category)
    )
    if not post_list:
        raise Http404
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list}
    )
