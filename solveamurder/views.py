from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import * 
# Create your views here.

login_url = 'login'


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

@login_required(login_url=login_url)
def editprofile(request):
    UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES , instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, "pages/profile.html", {"form": form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.get_or_create(user=request.user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'pages/register.html', {'form': form})