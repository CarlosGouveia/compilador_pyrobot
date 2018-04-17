from django import forms
from django.conf import settings


class cpf_form(forms.Form):

    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o cpf aqui'}),
                          max_length=50)

    class Meta:
        fields = ['cpf']


class expressao_form(forms.Form):
    expressao = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a expressao aqui'}),
        max_length=100)

    class Meta:
        fields = ['expressao']

class compilador_form(forms.Form):
    compilador = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'rows': '10',
                                     'cols': '80',
                                     'resize': 'none',
                                     'placeholder': 'Digite o codigo aqui'}))
    # compilador = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'form-group',
    #                                  'wrap': 'off',
    #                                  'autocorrect': 'off',
    #                                  'autocaptalize': 'off',
    #                                  'spellcheck': 'false',
    #                                  'placeholder': 'Digite o codigo aqui'}))

    # widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '10', 'cols': '80', 'resize': 'none',
    #                                'placeholder': 'Digite o codigo aqui'}))

    class Meta:
        fields = ['compilador']