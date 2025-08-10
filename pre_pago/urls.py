from django.urls import path
from . import views

app_name = "pre_pago"

urlpatterns = [
    #       Início
    path('', views.index, name="index"),
    
    #       Sessão
    path('cadastro', views.cadastro, name="cadastro"),
    path('login', views.login, name="login"),
    
    #       Conteúdo
    path('home', views.home, name="home"),
    path('historico', views.historico_de_pagamentos, name="historico"),
    path('perfil', views.perfil, name="perfil"),
    
    #       Sobre
    path('ajuda', views.ajuda, name="ajuda"),
    path('devs', views.desenvolvedores, name="devs"),
]