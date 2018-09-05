from django.shortcuts import render
from .models import Shohin

def index(request):
    return render(request, 'index.html')

def query(request):
    queryset = Shohin.objects.all()
    context = {  "queryset":queryset }
    return render(request, 'query.html', context)
