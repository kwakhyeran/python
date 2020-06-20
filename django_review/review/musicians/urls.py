from django.urls import path
from . import views

app_name = "musicians"

urlpatterns = [
    #u - v -t 순서 고정
    # pathname을 무엇으로 지었는지,
    # 어떤 view함수를 실행하는지
    # 하나의 경로에 하나의 view 함수
    path('',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('<int:musician_pk>/',views.detail,name="detail"),
    path('update/<int:musician_pk>',views.update,name="update"),
    path('delete/<int:musician_pk>',views.delete,name="delete"),
]