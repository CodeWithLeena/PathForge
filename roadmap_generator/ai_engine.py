import anthropic
import json
import re
from django.conf import settings


def generate_roadmap_with_ai(current_skills: str, target_job: str, experience_level: str, duration: str) -> dict:
    """Generate a personalized job roadmap using Claude AI."""
    
    duration_map = {
        '3months': '3 months (12 weeks)',
        '6months': '6 months (26 weeks)',
        '1year': '1 year (52 weeks)',
        '2years': '2 years (104 weeks)',
    }
    
    duration_text = duration_map.get(duration, '6 months (26 weeks)')
    
    prompt = f"""You are PathForge AI — an expert career roadmap architect. Generate a detailed, actionable skill-to-job roadmap.

USER PROFILE:
- Current Skills: {current_skills}
- Target Job Role: {target_job}
- Experience Level: {experience_level}
- Desired Duration: {duration_text}

Generate a comprehensive JSON roadmap with EXACTLY this structure:
{{
  "title": "Your personalized roadmap title",
  "overview": "2-3 sentence overview of this career path",
  "target_role": "{target_job}",
  "total_weeks": <number>,
  "difficulty_score": <1-10>,
  "salary_range": "estimated salary range in INR/USD",
  "job_demand": "High/Medium/Low",
  "key_outcomes": ["outcome1", "outcome2", "outcome3", "outcome4"],
  "phases": [
    {{
      "phase_number": 1,
      "title": "Phase title",
      "duration": "X weeks",
      "weeks_range": "Week 1-X",
      "description": "What this phase covers",
      "color": "#hex_color",
      "icon": "emoji_icon",
      "skills": [
        {{
          "name": "Skill name",
          "type": "Core/Advanced/Tool/Soft Skill",
          "hours": <estimated_hours>,
          "priority": "Must-Have/Nice-to-Have",
          "resources": [
            {{"title": "Resource name", "type": "Free/Paid", "url_hint": "platform name"}}
          ]
        }}
      ],
      "projects": [
        {{
          "title": "Project title",
          "description": "Brief project description",
          "difficulty": "Easy/Medium/Hard",
          "skills_used": ["skill1", "skill2"]
        }}
      ],
      "milestones": ["milestone1", "milestone2"]
    }}
  ],
  "top_companies": ["Company1", "Company2", "Company3", "Company4", "Company5"],
  "interview_prep": {{
    "topics": ["topic1", "topic2", "topic3"],
    "tips": ["tip1", "tip2", "tip3"]
  }},
  "certifications": [
    {{"name": "Cert name", "provider": "Provider", "priority": "High/Medium/Low"}}
  ]
}}

Make it specific, practical, and tailored to the Indian tech market. Include 3-5 phases. Respond with ONLY the JSON, no markdown."""

    try:
        api_key = settings.ANTHROPIC_API_KEY
        if not api_key:
            return get_fallback_roadmap(target_job, current_skills, duration)
        
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response_text = message.content[0].text.strip()
        
        # Clean any markdown fences
        response_text = re.sub(r'^```json\s*', '', response_text, flags=re.MULTILINE)
        response_text = re.sub(r'^```\s*', '', response_text, flags=re.MULTILINE)
        response_text = response_text.strip()
        
        roadmap_data = json.loads(response_text)
        return roadmap_data
        
    except Exception as e:
        print(f"AI Error: {e}")
        return get_fallback_roadmap(target_job, current_skills, duration)


def get_fallback_roadmap(target_job: str, current_skills: str, duration: str) -> dict:
    """Fallback roadmap when API is not configured."""
    return {
        "title": f"Complete Roadmap to Become a {target_job}",
        "overview": f"This comprehensive roadmap will guide you from your current skill set to landing a {target_job} role. Following this structured path will maximize your chances of success in the competitive tech market.",
        "target_role": target_job,
        "total_weeks": 26,
        "difficulty_score": 7,
        "salary_range": "₹8L - ₹25L per annum",
        "job_demand": "High",
        "key_outcomes": [
            f"Master core {target_job} skills",
            "Build 5+ portfolio projects",
            "Get industry-recognized certifications",
            "Land your first job interview"
        ],
        "phases": [
            {
                "phase_number": 1,
                "title": "Foundation Building",
                "duration": "6 weeks",
                "weeks_range": "Week 1-6",
                "description": "Establish strong fundamentals and core concepts",
                "color": "#6366f1",
                "icon": "🏗️",
                "skills": [
                    {
                        "name": "Core Programming Concepts",
                        "type": "Core",
                        "hours": 40,
                        "priority": "Must-Have",
                        "resources": [
                            {"title": "Python for Everybody", "type": "Free", "url_hint": "Coursera"},
                            {"title": "The Odin Project", "type": "Free", "url_hint": "theodinproject.com"}
                        ]
                    },
                    {
                        "name": "Data Structures & Algorithms",
                        "type": "Core",
                        "hours": 30,
                        "priority": "Must-Have",
                        "resources": [
                            {"title": "LeetCode Easy Problems", "type": "Free", "url_hint": "leetcode.com"},
                            {"title": "CS50 Harvard", "type": "Free", "url_hint": "edx.org"}
                        ]
                    }
                ],
                "projects": [
                    {
                        "title": "Personal Portfolio Website",
                        "description": "Build a responsive portfolio to showcase your journey",
                        "difficulty": "Easy",
                        "skills_used": ["HTML", "CSS", "JavaScript"]
                    }
                ],
                "milestones": ["Complete 20 coding challenges", "Deploy first project online"]
            },
            {
                "phase_number": 2,
                "title": "Core Skills Development",
                "duration": "10 weeks",
                "weeks_range": "Week 7-16",
                "description": "Deep dive into the primary technologies required for the role",
                "color": "#8b5cf6",
                "icon": "⚡",
                "skills": [
                    {
                        "name": f"{target_job} Core Technologies",
                        "type": "Core",
                        "hours": 60,
                        "priority": "Must-Have",
                        "resources": [
                            {"title": "Official Documentation", "type": "Free", "url_hint": "Official docs"},
                            {"title": "Udemy Course", "type": "Paid", "url_hint": "udemy.com"}
                        ]
                    },
                    {
                        "name": "Version Control (Git/GitHub)",
                        "type": "Tool",
                        "hours": 15,
                        "priority": "Must-Have",
                        "resources": [
                            {"title": "GitHub Learning Lab", "type": "Free", "url_hint": "github.com"}
                        ]
                    }
                ],
                "projects": [
                    {
                        "title": "Full-Featured Application",
                        "description": f"Build a complete {target_job}-relevant application from scratch",
                        "difficulty": "Medium",
                        "skills_used": ["Core Tech Stack", "Git", "Deployment"]
                    }
                ],
                "milestones": ["Complete main technology tutorial", "Build and deploy 2 projects"]
            },
            {
                "phase_number": 3,
                "title": "Advanced & Specialization",
                "duration": "6 weeks",
                "weeks_range": "Week 17-22",
                "description": "Advanced topics and industry best practices",
                "color": "#a855f7",
                "icon": "🚀",
                "skills": [
                    {
                        "name": "System Design Basics",
                        "type": "Advanced",
                        "hours": 25,
                        "priority": "Must-Have",
                        "resources": [
                            {"title": "System Design Primer", "type": "Free", "url_hint": "GitHub"}
                        ]
                    },
                    {
                        "name": "Cloud Basics (AWS/GCP/Azure)",
                        "type": "Tool",
                        "hours": 20,
                        "priority": "Nice-to-Have",
                        "resources": [
                            {"title": "AWS Free Tier", "type": "Free", "url_hint": "aws.amazon.com"}
                        ]
                    }
                ],
                "projects": [
                    {
                        "title": "Capstone Project",
                        "description": "End-to-end project demonstrating all acquired skills",
                        "difficulty": "Hard",
                        "skills_used": ["Full Stack", "Cloud", "Best Practices"]
                    }
                ],
                "milestones": ["Deploy cloud-based project", "Get first freelance client or contribution"]
            },
            {
                "phase_number": 4,
                "title": "Job Preparation",
                "duration": "4 weeks",
                "weeks_range": "Week 23-26",
                "description": "Interview prep, resume polish, and active job hunting",
                "color": "#c084fc",
                "icon": "🎯",
                "skills": [
                    {
                        "name": "Interview Preparation",
                        "type": "Soft Skill",
                        "hours": 30,
                        "priority": "Must-Have",
                        "resources": [
                            {"title": "Pramp Mock Interviews", "type": "Free", "url_hint": "pramp.com"},
                            {"title": "InterviewBit", "type": "Free", "url_hint": "interviewbit.com"}
                        ]
                    },
                    {
                        "name": "LinkedIn & Networking",
                        "type": "Soft Skill",
                        "hours": 10,
                        "priority": "Must-Have",
                        "resources": [
                            {"title": "LinkedIn Optimization Guide", "type": "Free", "url_hint": "linkedin.com"}
                        ]
                    }
                ],
                "projects": [
                    {
                        "title": "Portfolio Polish",
                        "description": "Refine all projects, write case studies, update resume",
                        "difficulty": "Easy",
                        "skills_used": ["Communication", "Documentation"]
                    }
                ],
                "milestones": ["Apply to 50+ jobs", "Complete 10 mock interviews", "Get first offer"]
            }
        ],
        "top_companies": ["TCS", "Infosys", "Wipro", "Flipkart", "Zomato"],
        "interview_prep": {
            "topics": ["Data Structures", "System Design", "Behavioral Questions", "Domain Knowledge"],
            "tips": [
                "Practice coding on a whiteboard/paper",
                "Research the company before interviews",
                "Prepare STAR format answers for behavioral questions"
            ]
        },
        "certifications": [
            {"name": "AWS Certified Developer", "provider": "Amazon", "priority": "High"},
            {"name": "Google Professional Certificate", "provider": "Google/Coursera", "priority": "Medium"}
        ]
    }
