from django.shortcuts import render

from django.http import HttpResponse
from .temp_data import post_data

def detail_post(request, post_id):
    post = post_data[post_id - 1]
    return HttpResponse(
        f'Detalhes do post {post["titulo"]} ({post["data_postagem"]})')

def list_posts(request):
    context = {"post_list": post_data}
    return render(request, 'posts/index.html', context)

def detail_post(request, post_id):
    context = {'post': post_data[post_id - 1]}
    return render(request, 'posts/detail.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "post_list": [
                m for m in post_data
                if request.GET['query'].lower() in m['titulo'].lower()
            ]
        }
    return render(request, 'posts/index.html', context)