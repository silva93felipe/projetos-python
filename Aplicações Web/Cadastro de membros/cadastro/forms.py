from django import forms
from . models import Membro, Cargo, Departamento

class InsereMembro(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ('nome', 'cpf', 'sexo', 'data_nascimento', 'cargo')



class InsereCargo(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ('descricao', )



class InsereDepartamento(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('descricao', )