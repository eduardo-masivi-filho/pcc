from django.db import models

class Sessao(models.Model):
    nome = models.CharField("nome_completo", max_length= 70)
    email = models.EmailField("email", max_length= 50)
    telefone= models.IntegerField("telefone")
    seu_id_na_provedoraa = models.IntegerField("seu_id_na_provedoraa")
    pin = models.IntegerField("pin")