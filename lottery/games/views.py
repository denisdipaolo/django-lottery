from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from games.models import Game

# Create your views here.
@login_required
def available_games_list(request):
	return render(request, 'games/games.html', {
        'available_games': Game.objects.available_games(request.user)
    })