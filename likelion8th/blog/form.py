from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta: #내부클래스
        model = Blog #blog를 기반으로 입력공간을 받음
        fields = ['title','body','image'] #모델 안에서 어떤 값들을 받을 건지 입력
        