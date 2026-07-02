from django.db import models
import json

class RoadmapRequest(models.Model):
    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner (0-1 years)'),
        ('intermediate', 'Intermediate (1-3 years)'),
        ('advanced', 'Advanced (3+ years)'),
    ]
    
    DURATION_CHOICES = [
        ('3months', '3 Months'),
        ('6months', '6 Months'),
        ('1year', '1 Year'),
        ('2years', '2 Years'),
    ]

    current_skills = models.TextField()
    target_job = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='beginner')
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES, default='6months')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.target_job} roadmap ({self.created_at.strftime('%d %b %Y')})"


class Roadmap(models.Model):
    request = models.OneToOneField(RoadmapRequest, on_delete=models.CASCADE, related_name='roadmap')
    title = models.CharField(max_length=300)
    overview = models.TextField()
    roadmap_data = models.TextField()  # JSON string
    total_weeks = models.IntegerField(default=0)
    difficulty_score = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_roadmap_data(self):
        try:
            return json.loads(self.roadmap_data)
        except:
            return {}

    def __str__(self):
        return self.title
