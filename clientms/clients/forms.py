from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Comment, Client, Vehicle
from django.contrib.auth import get_user_model


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['client', 'comment', 'author']
        exclude = ('client', )


