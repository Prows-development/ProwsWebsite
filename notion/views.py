from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def notion(request):
    return render(request, 'notion/index.html')