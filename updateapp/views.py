from django.shortcuts import redirect, render
from .forms import ProdutoForm
from django.urls import reverse_lazy
from .models import Produtos

def base(request):
    return render(request,'base.html')

def index(request):
    #Coloco esse codigo quando tudo estiver pronto, ele serve para mostra as imagens#
    data = Produtos.objects.all()
    #Ate aqui#
    return render(request,'index.html',{'data':data})

def home(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('produtos:index'))
    else:
        form = ProdutoForm()
            
    return render(request,'home.html',{'form':form})
