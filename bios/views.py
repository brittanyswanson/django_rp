from django.shortcuts import render
from .models import Character

# Create your views here.
def character_list(request):
    characters = Character.objects.order_by('first_name')
    return render(request,'bios/character_list.html',{'characters':characters})
