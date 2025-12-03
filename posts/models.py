from django.db import models
from django.conf import settings


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    data_postagem = models.IntegerField()
    imagem_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.titulo} ({self.data_postagem})'


class Review(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.autor.username}'