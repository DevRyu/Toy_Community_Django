from django.db import models
# Create your models here.


class Board(models.Model):  # 모델을 상속받아야한다
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    # 내용은 제약이없다.
    writer = models.ForeignKey(
        'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자')
    # fcuser에 기본키를 가져온다 //모델이 삭제가되면 같이 삭제하겟다라는 케스케이드
    # 사용자가 탈퇴하면 글도 같이 삭제하겟다는 말임
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title  # 클래스를  문자열로 직접변환하는 내장함수 Fcusers

    class Meta:  # 클래스내 클래스에서 테이블명을 지정 가능 이유는기본앱들과 구분되는 앱을 만들기위해서

        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'
    # 위의구문으로 SQL구문을 쓸필요 없이 다 설정이 된것임
