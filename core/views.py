from django.shortcuts import render, get_object_or_404
from core.models import Speaker

# Create your views here.
def home(request):
    speakers = [
        {'name':'Grace Hopper', 'photo': 'https://cleberfonseca.com.br/img/hopper.jpeg'},
        {'name':'Alan Turing', 'photo': 'https://cleberfonseca.com.br/img/turing.jpeg'}
    ]
    return render(request, 'index.html', {'speakers': speakers})

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})