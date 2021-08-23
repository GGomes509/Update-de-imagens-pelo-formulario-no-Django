from django import forms
from django.forms import widgets
from django.forms.widgets import ClearableFileInput, Widget
from .models import Produtos


class ProdutoForm(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput)
    class Meta:
        model=Produtos

        fields = '__all__'
        widgets={
            'nome':forms.TextInput(attrs={
                'maxlength':255,
                'placeholder':'Digite aqui canpeão'
            })            
        }