from django import forms
# from ..models import


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=6, required=True,
                               error_messages={"required": "用户账号不能为空",
                                               'invalid': "格式错误"},
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    passwd = forms.CharField(max_length=20, min_length=6,
                             widget=forms.PasswordInput(attrs={"class": "form-control"}))


class RegisterForm(forms.Form):
    userEmail = forms.CharField(max_length=100, min_length=6, required=True,
                                error_messages={"required":"用户邮箱不能为空",
                                                "invalid":"格式错误"},
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=20, min_length=6, required=True,
                               error_messages={"required": "用户账号不能为空",
                                               'invalid': "格式错误"},
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    passwd = forms.CharField(max_length=20, min_length=6,
                             widget=forms.PasswordInput(attrs={"class": "form-control"}))