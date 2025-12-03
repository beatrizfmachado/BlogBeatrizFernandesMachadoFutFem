from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .temp_data import post_data
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

#View READ para consulta de post
def list_posts(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)

#View para detalhamento de post
def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

#View para busca de post
def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

#View para criar post
def create_post(request):
    if request.method == 'POST':
        post_titulo = request.POST['titulo']
        post_data_postagem = request.POST['data_postagem']
        post_imagem_url = request.POST['imagem_url']
        post = Post(titulo=post_titulo,
                      data_postagem=post_data_postagem,
                      imagem_url=post_imagem_url)
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})
    

#View para atualizar post
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.titulo = request.POST['titulo']
        post.data_postagem = request.POST['data_postagem']
        post.imagem_url = request.POST['imagem_url']
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'posts/update.html', context)

#View para remover post
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)