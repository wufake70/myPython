# _*_coding :utf-8 _*_
# @Time :2022/9/20 16:36
# @File : form.py
# @Project : python_Django

from django import forms


class RegisterFrom(forms.Form):
    name = forms.CharField(max_length=50, min_length=6)
    pwd = forms.CharField(max_length=50, min_length=8,
                          widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}),
                          error_messages={'min_length': '密码长度不能少于8',
                                          'max_length': '密码长度不能大于50'})

    pwd_repeat = forms.CharField(max_length=50, min_length=8,
                                 widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}),
                                 error_messages={'min_length': '密码长度不能少于8',
                                                 'max_length': '密码长度不能大于50'})

    email = forms.EmailField()
