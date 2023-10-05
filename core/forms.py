from django import forms
from .models import Alimentos

class AlimentosForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ['nome', 'descricao', 'calorias']  # Liste todos os campos que deseja incluir no formulário
