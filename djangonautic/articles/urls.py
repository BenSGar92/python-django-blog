from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create', views.article_create, name='create'),
    path('<slug:slug>/', views.article_detail, name="detail"),
]
#first slug variable references the name of what is being passed to views.py in the article_detail function, send slug can be named anything else