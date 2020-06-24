from django import forms
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # article만 제외하고 다 가져오기
        # fields = '__all__'은 article도 포함해서 가져온다.
        exclude = ['article','user']