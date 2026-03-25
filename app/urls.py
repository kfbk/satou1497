from django.urls import path
from app import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('', views.StoreView.as_view(), name='store'),
    path('', views.videos_view, name='videos'),
    # path('video/<int:pk>/', views.video_view, name='video'),
]
