from django.shortcuts import render
from . import formularios
from .models import Sessao


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
    form = formularios.FormLogin()
    
    return render(request, "pre_pago/sessao/login.html", {
        "form": form
    })

def auth(request):
    
    nova_sessao = Sessao()
    
    nova_sessao.nome = request.POST.get("nome")
    nova_sessao.email = request.POST.get("email")
    nova_sessao.telefone = request.POST.get("telefone")
    nova_sessao.seu_id_na_provedoraa = request.POST.get("seu_id_na_provedoraa")
    nova_sessao.pin = request.POST.get("pin")
    cpin = request.POST.get("cpin")
    
    if cpin != nova_sessao.pin:
        return render(request, "pre_pago/sessao/cadastro.html", {
            "form" : formularios.FormCadastro(request.POST)
        })
    else:
        nova_sessao.save()
    
    return render(request, "pre_pago/sessao/auth.html",{
        "auth": formularios.FormAuth()
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
