from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    diretor = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    duracao = models.IntegerField()

    def __str__(self):
        return self.titulo
