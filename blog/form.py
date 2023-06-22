from django import forms
from mdeditor.fields import MDTextFormField
from .models import Articles


class ArticleForm(forms.ModelForm):
    """文章表单"""

    class Meta:
        model = Articles
        fields = ['title', 'text', 'meta_top', 'meta_second', 'public']
        labels = {'text': '', 'title': ''}
