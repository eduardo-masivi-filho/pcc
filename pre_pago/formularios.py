from django import forms

class FormCadastro(forms.Form):
    nome = forms.CharField(
        label="Nome Completo: ", 
        widget= forms.TextInput(), 
        max_length= 70
    )

    email = forms.EmailField(
        label="Email: ", 
        widget=forms.EmailInput(), 
        max_length= 50
    )
    
    telefone = forms.IntegerField(
        label="Nº de telefone: ", 
        widget=forms.NumberInput(), 
        max_value= 999999999
    )
    
    seu_id_na_provedoraa = forms.IntegerField(
        label="ID salvo na provedora: ", 
        widget=forms.NumberInput(), 
        max_value= 99999999
    )
    
    pin = forms.IntegerField(
        label="PIN", 
        widget=forms.PasswordInput(),
        max_value= 9999
    )

    cpin = forms.IntegerField(
        label="Confirmar PIN", 
        widget=forms.PasswordInput(),
        max_value= 9999
    )

class FormLogin(forms.Form):
    nome = forms.CharField(
        label="Nome Completo: ", 
        widget= forms.TextInput(), 
        max_length= 70
    )
    
    pin = forms.IntegerField(
        label="PIN", 
        widget=forms.PasswordInput(),
        max_value= 9999
    )

class FormAuth(forms.Form):
    Codigo_valido = forms.IntegerField(max_value = 9999)
