from django import forms
from django.forms import ModelForm
from .models import Artikel

class ArtikelForm(ModelForm):
    class Meta:
        model = Artikel
        fields = [
            'title', 'body', 'kategori'
        ]

        labels={
            'title':'Judul Artikel',
            'body':'Detail'
        }

        widgets={
            'title':forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'body':forms.Textarea(
                attrs={
                    'class':'form-control',
                }
            ),
            
            'kategori':forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
        }