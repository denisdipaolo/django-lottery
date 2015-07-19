from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PartecipationForm
from .models import Partecipation
# Create your views here.

@login_required
def partecipation(request, game_id=None):
    if request.method == 'POST':

        partecipation_form = PartecipationForm(data=request.POST, user=request.user)

        if partecipation_form.is_valid():
            partecipation = partecipation_form.save(commit=False)
            partecipation.user = request.user
            partecipation.save()

            return redirect('partecipation:confirmation')
    else:
        partecipation_form = PartecipationForm(initial={'game': game_id }, user=request.user)

    return render(request, 'partecipation/partecipation.html', {
        'partecipation_form': partecipation_form,
        'user_partecipations': Partecipation.objects.filter(user=request.user)
    })

@login_required
def confirmation(request):
    return render(request, 'partecipation/confirmation.html')
