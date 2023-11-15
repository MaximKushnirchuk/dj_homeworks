from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = "articles/news.html"
    list_objects = Article.objects.all()

    context = {"object_list": list_objects}
    return render(request, template, context)
