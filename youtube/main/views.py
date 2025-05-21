from django.shortcuts import render
from .models import Video

# Create your views here.
def home(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'main/home.html', context)

def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        uploaded_by = request.POST.get('uploaded_by')
        video_file = request.FILES.get('video_file')
        thumbnail = request.FILES.get('thumbnail')
        
        if title and description and uploaded_by and video_file:
            video = Video(
                title=title,
                description=description,
                uploaded_by=uploaded_by,
                video_file=video_file,
                thumbnail=thumbnail
            )
            video.save()
            return render(request, 'main/home.html', {'video': video})
        else:
            error = "All fields are required."
            return render(request, 'main/upload_video.html', {'error': error})
        
    return render(request, 'main/upload_video.html')


def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    context = {'video': video}
    return render(request, 'main/player.html', context)

# Add a search function to filter videos by title
def search_videos(request):
    query = request.GET.get('query')
    if query:
        videos = Video.objects.filter(title__icontains=query)
    else:
        videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'main/search_results.html', context) 