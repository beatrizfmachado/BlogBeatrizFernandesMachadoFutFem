from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .temp_data import post_data
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm
from django.views import generic


#Classe genérica com a view LIST para consulta de posts
class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'


#Classe genérica com a view DETAIL para detalhamento de post
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'


#View para busca de post
def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)


#Classe genérica com a view CREATE para criar post
class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    def get_success_url(self):
        return reverse_lazy('posts:detail', args=[self.object.id])
    

#Classe genérica com a view UPDATE para atualizar post
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'
    def get_success_url(self):
        return reverse_lazy('posts:detail', args=[self.object.id])


#Classe genérica com a view DELETE para remover post
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')