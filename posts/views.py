from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import post_data
from django.http import HttpResponseRedirect
from django.urls import reverse


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
    return render(request, 'posts/search.html', context)

def create_post(request):
    if request.method == 'POST':
        post_data.append({
            'titulo': request.POST['titulo'],
            'data_postagem': request.POST['data_postagem'],
            'imagem_url': request.POST['imagem_url']
        })
        return HttpResponseRedirect(
            reverse('posts:detail', args=(len(post_data), )))
    else:
        return render(request, 'posts/create.html', {})