from django.shortcuts import render
from .models import *


def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'index.html')

def clublar(request):
    content = {
        'clubs' : Club.objects.all()
    }
    return render(request,'clubs.html',content)

def ohirgi_transferlar(request):
    data = {
        'transfers': Transfer.objects.filter(mavsum = HozirgiMavsum.objects.order_by('mavsum').last())
    }
    return render(request,'latest-transfers.html',data)

def players(request):
    data={
        'players': Player.objects.all()
    }
    return render(request,'players.html',data)

def clublar_davlat(request,davlat):
    data = {
        'clubs' : Club.objects.filter(davlat= davlat)
    }
    return render(request,'england.html',data)

def sezon17_18(request,mavsum):
    content = {
        'transfers': Transfer.objects.filter(mavsum=mavsum)
    }
    return render(request,'2017-18season.html',content)

def u20_players(request):
    data = {
        'players': Player.objects.filter(t_yil__gt='2002-01-01').order_by('-tr_narx')
    }
    return render(request,'U-20 players.html',data)

def country_clubs(request,club):
    content = {
        'players': Player.objects.filter(club__nom=club)
    }
    return render(request,'country-clubs.html',content)