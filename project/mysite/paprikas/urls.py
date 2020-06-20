from django.urls import path
from . import views

app_name = "paprikas"

urlpatterns = [
    path('', views.main, name="main"),
    path('create/',views.create,name="create"),
    path('index/',views.index,name ="index"),

]