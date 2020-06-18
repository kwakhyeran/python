from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('movies/detail/<int:movie_pk>',views.detail,name="detail"),
    path('movies/<int:movie_pk>/edit/',views.edit,name ="edit"),
]