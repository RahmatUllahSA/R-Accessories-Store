from django.shortcuts import render
from django.http import HttpResponse # Import HttpResponse if needed

# Create your views here.

def my_view(request):
    return render(request, 'home.html', {})