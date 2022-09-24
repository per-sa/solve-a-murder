from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    total_suspects = Suspect.objects.all().count()
    total_victims = Victim.objects.all().count()
    total_unsolved = Cases.objects.filter(is_unsolved=True).count()
    context = {
        'total_suspects': total_suspects,
        'total_victims': total_victims,
        'total_unsolved': total_unsolved,
    }

    return render(request, 'pages/index.html', context)

def victims(request):
    victims = Victim.objects.all()
    context = {
        'victims': victims,
    }

    return render(request, 'pages/victims.html', context)