from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    limit = 12
    posts = Post.objects.all()[:limit]
    return render(request, "index.html", {"posts": posts})


def group_posts(request, slug, ):
    limit = 12
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:limit]
    return render(request, "group.html", {"group": group, "posts": posts})
