from django.shortcuts import render


def index(request):
    return render(request, 'cars/index.html')


def contact(request):
    return render(request, 'cars/contact.html')


def game(request):
    return render(request, 'cars/game.html')