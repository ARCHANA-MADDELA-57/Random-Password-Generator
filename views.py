from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialcharacter'):
        characters.extend(list('`~!@#$%^&*()_-'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    random_password = ''
    for i in range(length):
        random_password += random.choice(characters)
    return render(request, 'show_password.html', {'password': random_password})