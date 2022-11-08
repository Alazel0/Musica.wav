from django import forms
from .models import Comentarios

class ComentForm(forms.ModelForm):
	class Meta:
		model = Crear_Comentarios
		fields = ['title', 'description', 'important']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			'important': forms.CheckboxInput(attrs={'class': 'form-check'})
		}