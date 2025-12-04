from django.db import models
from django.conf import settings


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    data_postagem = models.DateTimeField()
    imagem_url = models.URLField(max_length=500, null=True)
    conteudo = models.TextField()

    def __str__(self):
        return f'{self.titulo} ({self.data_postagem})'


class Comment(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_comentario = models.DateTimeField()
    def __str__(self):
        return f'"{self.text}" - {self.autor.username}'