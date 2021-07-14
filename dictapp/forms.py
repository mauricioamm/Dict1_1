from django.forms import ModelForm, Textarea
from django import forms
from .models import dictclass

class DictForm(forms.ModelForm):
    class Meta:
        model = dictclass
        fields = ['id', 'Ordem', 'palavra', 'palavratrad', 'frase', 'frasetrad', 'frase2',
                  'frasetrad2', 'frase3', 'frasetrad3',
                  'figura1', 'som1', 'suaresposta1', 'suaresposta2', 'suaresposta3']
        #'tipo_audio'
        #TIPOAUDIO = [('ingles', 'ingles'), ('alemao', 'alemao')]

        widgets = {'id': forms.TextInput(attrs={'size': 5}),
                   'Ordem': forms.TextInput(attrs={'size': 70}),
                   'palavra': forms.TextInput(attrs={'size': 70}),
                   'palavratrad': forms.TextInput(attrs={'size': 70}),
                   'frase': forms.TextInput(attrs={'size': 70}),
                   'frasetrad': forms.TextInput(attrs={'size': 70}),
                   'frase2': forms.TextInput(attrs={'size': 70}),
                   'frasetrad2': forms.TextInput(attrs={'size': 70}),
                   'frase3': forms.TextInput(attrs={'size': 70}),
                   'frasetrad3': forms.TextInput(attrs={'size': 70}),
                   'figura1': forms.TextInput(attrs={'size': 70}),
                   'som1': forms.TextInput(attrs={'size': 70}),
                   'suaresposta1': forms.TextInput(attrs={'size': 70}),
                   'suaresposta2': forms.TextInput(attrs={'size': 70}),
                   'suaresposta3': forms.TextInput(attrs={'size': 70}),

                   }

class DictForm2(forms.ModelForm):
    class Meta:
        model = dictclass
        fields = ['suaresposta1']
        widgets = {'suaresposta1': forms.TextInput(attrs={'size': 70}),}



"""
class TipoAudio(forms.ModelForm):
    TIPOAUDIO = [('ingles', 'ingles'), ('alemao', 'alemao')]
    campo_doisaudios = forms.CharField(widget=forms.RadioSelect(choices=TIPOAUDIO))

    class Meta:
        model = ForensicTraffic
        fields = ['campo_doisaudios']
"""