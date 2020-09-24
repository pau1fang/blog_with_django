from django.urls import path
from . import views


app_name = 'comments'

urlpatterns = [
    path('post-comment/<int:article_id>/', views.CommentPostView.as_view(), name='post_comment'),
    path(
        'post-comment/<int:article_id>/<int:parent_comment_id>',
        views.CommentPostView.as_view(),
        name='comment_reply'
    ),
]
