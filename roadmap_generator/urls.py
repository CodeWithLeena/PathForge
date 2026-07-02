from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_roadmap, name='generate_roadmap'),
    path('roadmap/<int:roadmap_id>/', views.roadmap_detail, name='roadmap_detail'),
    path('explore/', views.explore, name='explore'),
    path('about/', views.about, name='about'),
]
