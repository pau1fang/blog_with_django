from .models import Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class CommentForm(forms.ModelForm):
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ['body']

