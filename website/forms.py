# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 11:52
# @Author  : 十忆九非
# @Email   : shiyijiufei@gmail.com
# @File    : forms.py
# @Software: PyCharm

from django import forms
from . models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
