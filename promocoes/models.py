from django.db import models
from produtos.models import Produto

# Create your models here.

# class Promocao(models.Model):
#     nome = models.CharField(max_length=255, blank=True)
#     produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
#     desconto = models.PositiveIntegerField()
#     preco = produto.value_from_object()

#     def __str__(self) -> str:
#         return f'{self.nome} R$ {self.preco}'