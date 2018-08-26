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


# 博客撰写页面
def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


# 博客撰写以及修改
def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)   # 写入数据库
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()    # 更新数据库
    return render(request, 'blog/article_page.html', {'article': article})


# 删除博客
def delete_article(request, article_id):
    article_id = request.POST.get(article_id, '0')
    models.Article.objects.filter(pk=str(article_id)).delete()

    return index(request)
