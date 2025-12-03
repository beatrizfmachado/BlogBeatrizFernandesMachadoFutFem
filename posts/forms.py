from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'data_postagem',
            'imagem_url',
        ]
        labels = {
            'titulo': 'Título',
            'data_postagem': 'Data do post',
            'imagem_url': 'URL da imagem do post',
        }