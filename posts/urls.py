from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('<int:post_id>/', views.detail_post, name='detail'),
]