from django.shortcuts import render, get_object_or_404

from .models import Group, Post

DEF_POST = 10


def index(request):
    posts = Post.objects.all()[:DEF_POST]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
