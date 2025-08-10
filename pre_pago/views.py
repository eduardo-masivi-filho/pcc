from django.shortcuts import render
from . import formularios

#       Início
def index(request):
    return render(request,"pre_pago/index.html")

#       Sessão
def cadastro(request):
    if request.method == "POST":
        form = formularios.FormCadastro(request.POST)
        
        if form.is_valid():
            form.cleaned_data

        else:
            return render(request, "pre_pago/sessao/cadastro.html", {
                "form": form
            })
            
    return render(request, "pre_pago/sessao/cadastro.html",{
        "form":formularios.FormCadastro()
    })

def login(request):
    return render(request, "pre_pago/sessao/login.html")

def verificar(request):
    return render(request, "pre_pago/sessao/verificar.html",{
        "verificar": formularios.FormValidar()
    })

#       Conteúdo
def home(request):
    return render(request, "pre_pago/conteudo/home.html")

def historico_de_pagamentos(request):
    return render(request, "pre_pago/conteudo/historico_pagamentos.html")

def perfil(request):
    return render(request, "pre_pago/conteudo/perfil.html")

#       Sobre
def ajuda(request):
    return render(request, "pre_pago/sobre/ajuda.html")

def desenvolvedores(request):
    return render(request, "pre_pago/sobre/devs.html")
