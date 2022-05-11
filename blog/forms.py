from django import forms

from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    tags = forms.CharField(max_length=200)

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
