from django.contrib import admin
from .models import RoadmapRequest, Roadmap

@admin.register(RoadmapRequest)
class RoadmapRequestAdmin(admin.ModelAdmin):
    list_display = ['target_job', 'experience_level', 'duration', 'created_at']
    list_filter = ['experience_level', 'duration']
    search_fields = ['target_job', 'current_skills']

@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_weeks', 'difficulty_score', 'created_at']
    search_fields = ['title']
