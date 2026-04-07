from django.shortcuts import render
from hexlet_django_blog.article.apps import ArticleConfig


def index(request):
    return render(
        request,
        "article/index.html",
        context={
            "app": ArticleConfig.name,
        },
    )