from django.shortcuts import render
from .models import Video

# Create your views here.
def home(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'main/home.html', context)