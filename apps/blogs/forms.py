#-*-coding:utf-8-*-
__author__: 'McEachen'
__date__: '2018/3/27 14:28'

from django import forms


class MessageForm(forms.Form):
    username = forms.CharField(required=True,min_length=5)
    email = forms.EmailField(required=True)
    content = forms.CharField(required=True,max_length=40)


