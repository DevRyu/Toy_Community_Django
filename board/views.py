from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from fcuser.models import Fcuser
from .forms import BoardForm
from .models import Board


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을수 없습니다')
    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login')  # 로그인에 성공하지 않았으면 로그인 화면으로 옮겨라
    if request.method == 'POST':  # post= create 일때 데이터를 넣음
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            # 글쓴이는 로그인할때의 세션데이터에 있다.
            fcuser = Fcuser.objects.get(pk=user_id)
            # 글쓴이를 pk라고 쓰겟다.
            board = Board()
            # 보드 모델(데이터)클래스를 클로저로
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
            # 결과를 저장한다
            return redirect('/board/list/')
            # 저장한 내용은 리다이렉트 함수로 /board/list/로 보내준다.
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    # 아이디 번호 순서대로 정렬헤서 가지고 오겟다라는 말
    # 페이지네이터 할때 기존의 변수를 all_boards로 바꿈
    page = int(request.GET.get('p', 1))
    # 페이지 번호를 get으로 번호를받음 기본값은 1번으로 숫자형으로 받음
    paginator = Paginator(all_boards, 2)
    # 총페이지는 2개로 클래스를 가지고 간단하게 패이즈를 받을수있음
    boards = paginator.get_page(page)
    # 위의 페이지를  페이지를해서 boards 변수에 저장 페이지 넘길때 사용할거임
    return render(request, 'board_list.html', {'boards': boards})
    # 템플릿에서 출력할수있는 보드즈 라는변수를 만듬
