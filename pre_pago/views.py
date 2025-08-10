from django.shortcuts import render

#       Início
def index(request):
    return render(request,"pre_pago/index.html")

#       Sessão
def cadastro(request):
    return render(request, "pre_pago/sessao/cadastro.html")

def login(request):
    return render(request, "pre_pago/sessao/login.html")

#       Conteúdo
def home(request):
    return render(request, "pre_pago/conteudo/home.html")

def historico_de_pagamentos(request):
    return render(request, "pre_pago/conteudo/historico_pagamentos.html")

def perfil(request):
    return render(request, "pre_pago/conteudo/perfil.html")
