from django import forms

from games.models import Game
from .models import Partecipation

class PartecipationForm(forms.ModelForm):
    game = forms.ModelChoiceField(queryset=None)

    def __init__(self, user, *args, **kwargs):
        super(PartecipationForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['game'].queryset = Game.objects.available_games(user)

    class Meta:
        model = Partecipation
        exclude = ('user',)