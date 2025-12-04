from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'conteudo',
            'data_postagem',
            'imagem_url',
        ]
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo(HTML)',
            'data_postagem': 'Data do post',
            'imagem_url': 'URL da imagem do post',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'autor',
            'text',
            'data_comentario',
        ]
        labels = {
            'autor': 'Usuário',
            'text': 'Comentário',
            'data_comentario': 'Data do comentário',
        }