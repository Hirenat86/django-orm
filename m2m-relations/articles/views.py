
from articles.models import Article
from django.shortcuts import render



def articles_list(request):
    template = 'articles/news.html'
    context = {"object_list": Article.objects.all().prefetch_related('scope')}
    return render(request, template, context)