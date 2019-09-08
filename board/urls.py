from django.urls import path
from . import views
urlpatterns = [
    path('detail/<int:pk>/', views.board_detail),
    # 정수형 숫자형인 pk를 받겟다. 받는곳은 views.py로부터
    path('list/', views.board_list),
    path('write/', views.board_write),
]
