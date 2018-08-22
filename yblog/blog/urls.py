from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),

    # Django 2.0 版本新特性  路由参数的变化（以前是(?P<article_id>[0-9]{4})）
    path('article/<int:article_id>', views.article_page, name='article_page'),
]
