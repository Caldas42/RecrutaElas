from django import forms

class ComentarioForm(forms.Form):
    comentario = forms.CharField(widget=forms.Textarea, max_length=500)
