from dataclasses import field
from msilib.schema import Class
from tkinter import Widget
from django import forms
from django.forms import ModelForm

from .models import crearCurso, Matricula

class crearCursoForms(ModelForm):
    class Meta:
        model = crearCurso
        fields = '__all__'
    # idCurso = forms.CharField(label='id curso', max_length=10, widget=forms.TextInput(attrs={'class': 'input'}))
    # nombreCurso = forms.CharField(label='Nombre del curso', max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    # numeroCreditos = forms.CharField(label='Numero de creditos', max_length=3, widget=forms.TextInput(attrs={'class': 'input'}))
    # tipoPrograma = forms.CharField(label='Tipo de programa', max_length=10, widget=forms.TextInput(attrs={'class': 'input'}))
    # programaPertenece = forms.CharField(label='Programa al que pertenece', max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    # semestre = forms.CharField(label='Semestre ', max_length=2, widget=forms.TextInput(attrs={'class': 'input'}))
    # descripcion = forms.CharField(label='Descripcion del curso', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))

class crearMatricula(ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'