from django.forms import ModelForm
from .models import Post


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