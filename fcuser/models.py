from django.db import models
# Create your models here.


class Fcuser(models.Model):  # 모델을 상속받아야한다
    username = models.CharField(max_length=32, verbose_name='사용자명')

    useremail = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    # fcuser 저장하는시점그대로 auto_now_add=True
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username  # 클래스를  문자열로 직접변환하는 내장함수 Fcusers

    class Meta:  # 클래스내 클래스에서 테이블명을 지정 가능 이유는기본앱들과 구분되는 앱을 만들기위해서

        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'
    # 위의구문으로 SQL구문을 쓸필요 없이 다 설정이 된것임
