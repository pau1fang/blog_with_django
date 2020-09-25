from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from account.models import BlogUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
import markdown
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from comments.models import Comment
from comments.forms import CommentForm
import logging


logger = logging.getLogger(__name__)


class ArticleList(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/articles.html'

    # 页面类型
    paginate_by = 5
    page_kwarg = 'page'
    s = ''

    def get_page_number(self):
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        return page

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-create_time')
        self.s = self.request.GET.get('s')
        if self.s:
            queryset = queryset.filter(
                Q(title__icontains=self.s) |
                Q(body__icontains=self.s)
            )
        else:
            self.s = ''
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update({'s': self.s})
        return context


class ArticleDetail(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blog/article_detail.html'

    def get_object(self, queryset=None):
        obj = super(ArticleDetail, self).get_object()
        obj.viewed()
        self.object = obj

        md = markdown.Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                TocExtension(slugify=slugify)
            ])

        obj.body = md.convert(obj.body)

        return obj

    def get_context_data(self, **kwargs):
        article_id = self.kwargs.get(self.pk_url_kwarg)
        if article_id:
            comments = Comment.objects.filter(article_id=article_id).order_by('-create_time')
            kwargs['comments'] = comments
            kwargs['comment_count'] = len(comments) if comments else 0
            kwargs['comment_form'] = CommentForm()
        return super(ArticleDetail, self).get_context_data(**kwargs)


# class ArticleCreated(generic.FormView):
#     form_class = ArticlePostForm
#     success_url = '/blog'
#     template_name = 'blog/article_created.html'
#
#     def form_valid(self, form):
#         user = self.request.user
#         # article_data = form.cleaned_data
#         new_article = form.save(commit=False)
#         new_article.author_id = user.id
#         new_article.save()
#         form.save_m2m()
#         return super().form_valid(form)
#
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         categorys = Category.objects.all()
#         context.update({'categorys': categorys})
#         return context
#
#     def get_form(self, form_class=None):
#         return super().get_form()





