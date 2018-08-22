from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    articles = models.Article.objects.all()    # 查询所有文章
    return render(request, 'blog/index.html', {'articles': articles})


# 根据文章id 查询文章内容
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
