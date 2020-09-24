from django import template
from django.shortcuts import reverse
register = template.Library()


@register.simple_tag
def root_comments(comments, **kwargs):
    return comments.filter(**kwargs)


@register.simple_tag
def child_comments(comment_list, comment):
    """获取当前评论子评论列表"""
    comments = []

    def parse(c):
        if c is None:
            childs = comment_list.filter(parent_comment=c)
        else:
            childs = comment_list.filter(parent_comment=c).order_by('create_time')
        for child in childs:
            comments.append(child)
            parse(child)

    parse(comment)
    return comments

