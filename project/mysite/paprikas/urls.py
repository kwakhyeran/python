from django.urls import path
from . import views

app_name = "paprikas"

urlpatterns = [
    path('', views.main, name="main"),
    path('create/',views.create,name="create"),
    path('index/',views.index,name ="index"),
    path('delete/<int:paprikas_pk>/',views.delete,name="delete"),
    path('update/<int:paprikas_pk>/',views.update,name="update"),
    path('detail/<int:paprikas_pk>/',views.detail,name="detail"),

]