from django.shortcuts import render

from django.http import HttpResponse
from .temp_data import post_data

def detail_post(request, post_id):
    post = post_data[post_id - 1]
    return HttpResponse(
        f'Detalhes do post {post["Título"]} ({post["Data da postagem"]})')
