from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.


def home(request):
    # 세션으로 부터 사용자 정보를 가져온다.
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)  # pk키로 설정
        return HttpResponse(fcuser.username)

    return HttpResponse('home!')


def logout(request):
    if request.session.get('user'):  # 로그인이유지되어있으면
        del(request.session['user'])  # user 세션을 삭제해서 로그아웃이되게하라
    return redirect('/')  # 그리고 리턴은 홈으로간다 템플릿이 필요없이 홈만가도록 하면됨 urls.py에만 정해주면도미


def login(request):
    if request.method == 'POST':  # 요청방법 포스트면
        form = LoginForm(request.POST)  # 폼에 데이터를넣고 정상적인지 검증하고
        if form.is_valid():  # 유효한지 세션코드를 넣고 검증하고 에러정보를 출력
            request.session['user'] = form.user_id
            return redirect('/')
    else:  # 유효한 정보가 아니면 에러메세지를 폼에 담음
        form = LoginForm()
    # 폼즈안에 로그인폼 가지고오고 클래스 변수를 만들고 템플릿전달
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':  # register.html에서 의 값을 받음
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든값을 입력해야합니다.'
        elif password != re_password:
            # return HttpResponse('비밀번호가 다릅니다.') 에러메세지 페이지로 이동함
            res_data['error'] = '비밀번호가 다릅니다'  # register.html에 {{error}} 삽입
        else:
            fcuser = Fcuser(  # 클래스를 가지고와서 변수를 선언
                username=username,
                # password=password 암호화 없이들어감
                useremail=useremail,
                password=make_password(password)
            )
            fcuser.save()  # 클래스의 객체 생성

        return render(request, 'register.html', res_data)
 # 폴더위치가 기존과 다르면 상대경로 지정해줘야함
