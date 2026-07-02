# ⬡ PathForge — AI Career Roadmap Generator

PathForge is a professional Django web application that uses Claude AI to generate personalized, week-by-week career roadmaps for tech professionals.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Your API Key
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```
Or copy `.env.example` to `.env` and fill in your key.

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Start the Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` 🎉

## ✨ Features

- **AI-Powered Roadmaps** — Claude AI generates personalized career paths
- **Phase-Based Learning** — Structured weeks with clear milestones
- **Skill Gap Analysis** — Identifies exactly what you need to learn
- **Project Ideas** — Real projects to build your portfolio
- **Interview Prep** — Role-specific tips and topics
- **Resource Curation** — Free & paid learning resources for each skill
- **Company Insights** — Top companies hiring for your target role

## 🛠️ Stack

- **Backend**: Django 4.2 (Python)
- **AI**: Anthropic Claude API
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Frontend**: Vanilla HTML/CSS/JS (no framework needed)

## 📁 Project Structure

```
PathForge/
├── pathforge/          # Django project settings
├── roadmap_generator/  # Main app
│   ├── models.py       # Database models
│   ├── views.py        # Route handlers
│   ├── ai_engine.py    # Claude AI integration
│   └── urls.py         # URL routing
├── templates/          # HTML templates
├── static/             # CSS, JS, images
└── requirements.txt
```

## 🔑 Admin Panel

```bash
python manage.py createsuperuser
# Visit http://localhost:8000/admin
```

## 🚀 Production Deployment

1. Set `DEBUG=False` in settings
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL for the database
4. Add WhiteNoise for static files
5. Deploy with Gunicorn + Nginx

---
Built with ♥ using Django + Claude AI
