from django.shortcuts import render
from produtos.models import Produto

# Create your views here.
def index(request):
    produtos = Produto.objects.filter(quantidade__gt=0)
    return render(request, "pages/home.html", {
        'produtos': produtos,
    })