from blog.models import Article
from .models import Comment
from .forms import CommentForm
from django.views import generic


class CommentPostView(generic.FormView):
    form_class = CommentForm
    template_name = 'comments/reply.html'
    success_url = ''

    def form_valid(self, form):
        user = self.request.user
        article_id = self.kwargs['article_id']
        article = Article.objects.get(pk=article_id)
        comment = form.save(commit=False)
        comment.article = article
        comment.author = user
        parent_comment_id = self.kwargs.get('parent_comment_id')
        if parent_comment_id:
            parent_comment = Comment.objects.get(pk=parent_comment_id)
            comment.parent_comment = parent_comment
            if parent_comment.parent_comment:
                comment.parent_comment = Comment.objects.get(pk=parent_comment.parent_comment.pk)
            comment.reply_to = parent_comment

        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article_id = self.kwargs['article_id']
        if article_id:
            self.success_url = f'/blog/article/{article_id}'
        return str(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs['article_id']
        parent_comment_id = self.kwargs['parent_comment_id']
        context['article_id'] = article_id
        context['parent_comment_id'] = parent_comment_id
        context['comment_form'] = CommentForm
        return context






