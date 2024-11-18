from django import forms
from .models import Character, Equipement

class MoveForm(forms.Form):
    id_character = forms.ModelChoiceField(queryset=Character.objects.all(), label="Id character")
    lieu = forms.ModelChoiceField(queryset=Equipement.objects.filter(disponibilite="Libre"), label="Lieu")
