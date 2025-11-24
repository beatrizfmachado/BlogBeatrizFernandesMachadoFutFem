from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.list_posts, name='index'),
    path('search/', views.search_posts, name='search'),
    path('<int:post_id>/', views.detail_post, name='detail'),
]