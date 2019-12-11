from django import forms
from .models import Match


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['game']
        widgets = {
            'game': forms.TextInput(attrs={'class': 'validate'}),
        }
