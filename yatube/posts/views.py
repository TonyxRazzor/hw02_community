from django.shortcuts import render, get_object_or_404

from .models import Group, Post

DEF_POST = 10


def index(request):
    posts = Post.objects.all()[:DEF_POST]
    title = 'Главная страница'
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.related_name.posts.all()[:10]
    title = 'Страница Групп'
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/group_list.html', context)
