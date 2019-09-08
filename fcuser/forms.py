"""
high level support for doing this and that.
"""
from django import forms
from django.contrib.auth.hashers import check_password
from .models import Fcuser


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        }, max_length=32, label="사용자이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        }, widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)  # 아이디 맞은부분
            except Fcuser.DoesNotExist:
                # 이모델에서 DoesNotExist가 나온다면
                self.add_error('username', '회원가입된 아이디가 아닙니다.')
                return
                # 리턴을 그냥 화면으로 나오게한다.
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:  # 아이디비밀번호 맞은부분
                self.user_id = fcuser.id
