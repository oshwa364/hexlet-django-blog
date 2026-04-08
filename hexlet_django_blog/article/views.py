from django.shortcuts import render
from hexlet_django_blog.article.apps import ArticleConfig
from django.views import View
from django.http import HttpResponse


class IndexView(View):
    template_name = 'article/index.html'

    def get(self, request, tags, article_id):
        return render(
            request,
            self.template_name,
            context={
                'tags': tags,
                'article_id': article_id,
            }
        )