from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'articles'

urlpatterns = [
    path(
        'articles',
        views.ArticleList.as_view(),
        name='article_list'
    ),

    path(
        'articles/page/<int:page>',
        views.ArticleList.as_view(),
        name='article_list'
    ),

    path(
        'article/<int:pk>',
        views.ArticleDetail.as_view(),
        name='article_detail'
    ),

    # path(
    #     'article/created/',
    #     login_required(views.ArticleCreated.as_view(), login_url='/account/login'),
    #     name='article_created'
    # ),

    path(
        '',
        views.ArticleList.as_view(),
        name='articles_list'
    ),

    path(
        'page/<int:page>',
        views.ArticleList.as_view(),
        name='articles_list'
    ),
]