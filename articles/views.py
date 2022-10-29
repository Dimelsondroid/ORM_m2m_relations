from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    news = [article for article in Article.objects.all()]
    context = {'object_list': news}

    return render(request, template, context)
