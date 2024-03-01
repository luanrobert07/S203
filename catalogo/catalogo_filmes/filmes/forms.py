from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'data_lancamento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'titulo': 'Título do Filme',
            'ano_lancamento': 'Ano de Lançamento',
            'diretor': 'Diretor(a)',
            'genero': 'Gênero',
            'duracao': 'Duração (minutos)',
            'data_lancamento': 'Data de Lançamento',
        }
        help_texts = {
            'titulo': 'Informe o título completo do filme.',
            'ano_lancamento': 'Informe o ano de lançamento do filme.',
            'diretor': 'Informe o nome do diretor(a) do filme.',
            'genero': 'Selecione o gênero do filme.',
            'duracao': 'Informe a duração do filme em minutos.',
            'data_lancamento': 'Selecione a data de lançamento do filme.',
        }

    def clean_duracao(self):
        duracao = self.cleaned_data['duracao']
        if duracao < 0:
            raise forms.ValidationError("A duração não pode ser negativa.")
        return duracao

class FilmeFilterForm(forms.Form):
    ordenar_por = forms.ChoiceField(choices=[('ano_lancamento', 'Ano de Lançamento'), ('genero', 'Gênero'), ('diretor', 'Diretor'), ('titulo', 'Título')])
    filtro_genero = forms.CharField(required=False)
    filtro_diretor = forms.CharField(required=False)