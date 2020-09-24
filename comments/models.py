from django.db import models
from django.conf import settings
from articles.models import Article
from django.utils.timezone import now
from ckeditor.fields import RichTextField


class Comment(models.Model):
    body = RichTextField()
    create_time = models.DateTimeField('创建时间', default=now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self',
        verbose_name='上级评论',
        related_name='%(class)s_child_comments',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    reply_to = models.ForeignKey(
        'self',
        verbose_name='回复给',
        related_name='%(class)s_rep_comments',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def __str__(self):
        return self.body

    def count(self):
        return len(Comment.objects.all())


