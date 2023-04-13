from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField(default=0)
    codigo = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome