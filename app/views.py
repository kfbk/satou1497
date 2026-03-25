from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import TemplateView, View
from app.models import Video
from django.contrib.auth.decorators import login_required   # ログイン機能

class IndexView(TemplateView):
    template_name = "app/index.html"


def videos_view(request):
  videos = Video.objects.all().order_by("-uploaded_at")
  context = {
    'videos' : videos,
  }
  return render(request, 'app/videos.html', context)

# @login_required
# def video_view(request, pk):
#   video = get_object_or_404(Video, id=pk)
#   # print(f'video = {video.file}')
#   context = {
#     'video' : video,
#   }
#   return render(request, 'app/video.html', context)
