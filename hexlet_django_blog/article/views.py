from django.shortcuts import render
from hexlet_django_blog.article.apps import ArticleConfig
from django.views import View
from django.http import HttpResponse


class IndexView(View):
    template_name = 'article/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self,):
        context = {}
        context['app'] = ArticleConfig.name
        return context