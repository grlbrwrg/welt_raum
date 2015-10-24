from django import forms
from .models import Events

class EventAuswahlForm(forms.Form):
    event = forms.ModelChoiceField(label='Veranstaltung auswählen', queryset=Events.objects.all())
