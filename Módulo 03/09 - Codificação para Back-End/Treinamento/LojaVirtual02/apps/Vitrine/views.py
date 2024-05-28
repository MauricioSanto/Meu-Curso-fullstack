from django.shortcuts import render


def Saudacao(request):
    return render(request, 'ola_mundo.html')
