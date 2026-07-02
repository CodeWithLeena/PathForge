from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import RoadmapRequest, Roadmap
from .ai_engine import generate_roadmap_with_ai


def home(request):
    recent_roadmaps = Roadmap.objects.order_by('-created_at')[:6]
    stats = {
        'total_roadmaps': Roadmap.objects.count(),
        'job_roles': Roadmap.objects.values('request__target_job').distinct().count(),
    }
    return render(request, 'pathforge/home.html', {
        'recent_roadmaps': recent_roadmaps,
        'stats': stats,
    })


@require_http_methods(["GET", "POST"])
def generate_roadmap(request):
    if request.method == 'POST':
        current_skills = request.POST.get('current_skills', '').strip()
        target_job = request.POST.get('target_job', '').strip()
        experience_level = request.POST.get('experience_level', 'beginner')
        duration = request.POST.get('duration', '6months')

        if not current_skills or not target_job:
            return render(request, 'pathforge/generate.html', {
                'error': 'Please fill in all required fields.',
                'form_data': request.POST,
            })

        # Save the request
        roadmap_request = RoadmapRequest.objects.create(
            current_skills=current_skills,
            target_job=target_job,
            experience_level=experience_level,
            duration=duration,
        )

        # Generate roadmap using AI
        roadmap_data = generate_roadmap_with_ai(
            current_skills=current_skills,
            target_job=target_job,
            experience_level=experience_level,
            duration=duration,
        )

        # Save the roadmap
        roadmap = Roadmap.objects.create(
            request=roadmap_request,
            title=roadmap_data.get('title', f'Roadmap to {target_job}'),
            overview=roadmap_data.get('overview', ''),
            roadmap_data=json.dumps(roadmap_data),
            total_weeks=roadmap_data.get('total_weeks', 26),
            difficulty_score=roadmap_data.get('difficulty_score', 5),
        )

        return redirect('roadmap_detail', roadmap_id=roadmap.id)

    return render(request, 'pathforge/generate.html')


def roadmap_detail(request, roadmap_id):
    roadmap = get_object_or_404(Roadmap, id=roadmap_id)
    data = roadmap.get_roadmap_data()
    return render(request, 'pathforge/roadmap_detail.html', {
        'roadmap': roadmap,
        'data': data,
        'phases': data.get('phases', []),
        'certifications': data.get('certifications', []),
        'top_companies': data.get('top_companies', []),
        'interview_prep': data.get('interview_prep', {}),
        'key_outcomes': data.get('key_outcomes', []),
    })


def explore(request):
    roadmaps = Roadmap.objects.order_by('-created_at')[:20]
    return render(request, 'pathforge/explore.html', {'roadmaps': roadmaps})


def about(request):
    return render(request, 'pathforge/about.html')
