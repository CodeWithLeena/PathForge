# ⬡ PathForge — AI Career Roadmap Generator

> **PathForge** is an AI-powered career planning platform built with **Django** that generates personalized, week-by-week learning roadmaps based on a user's target career, current skill set, and experience level.

Designed for students, freshers, and professionals, PathForge helps users identify skill gaps, build job-ready projects, prepare for interviews, and follow a structured roadmap to achieve their career goals.

---

# 🚀 Features

* 🤖 AI-generated personalized career roadmaps
* 📅 Week-by-week learning plans with milestones
* 🎯 Skill gap analysis and improvement suggestions
* 💼 Real-world portfolio project recommendations
* 🎤 Interview preparation guidance
* 📚 Curated learning resources (Free & Paid)
* 🏢 Top companies hiring for your target role
* 📈 Structured learning phases
* 🔐 Secure authentication and user management
* ⚡ Fast, responsive, and clean user interface

---

# 🛠️ Tech Stack

| Technology               | Description                                    |
| ------------------------ | ---------------------------------------------- |
| **Backend**              | Django 4.2 (Python)                            |
| **Programming Language** | Python                                         |
| **Database**             | SQLite (Development) / PostgreSQL (Production) |
| **Frontend**             | HTML5, CSS3, JavaScript                        |
| **Deployment**           | Gunicorn, WhiteNoise, Nginx                    |

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/CodeWithLeena/PathForge.git

cd PathForge
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root and add:

```env
API_KEY=your_api_key_here
```

---

### 4️⃣ Run Database Migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Start the Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

# 📂 Project Structure

```text
PathForge/
│
├── pathforge/
├── roadmap_generator/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── ai_engine.py
│   └── forms.py
│
├── templates/
├── static/
├── media/
├── requirements.txt
├── manage.py
└── README.md
```

---

# 🚀 Production Deployment

Before deploying:

* Set `DEBUG = False`
* Configure `ALLOWED_HOSTS`
* Use PostgreSQL database
* Configure environment variables
* Serve static files using WhiteNoise
* Deploy with Gunicorn + Nginx

---

# 🎯 Future Enhancements

* Resume Analyzer
* ATS Resume Score
* AI Cover Letter Generator
* Job Matching
* Resume Builder
* Progress Tracking Dashboard
* Learning Analytics
* Multiple AI Model Support

---

# 🤝 Contributing

Contributions, feature requests, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 👩‍💻 Author

**Leena Jain**

GitHub: **https://github.com/CodeWithLeena**

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

**Developed with ❤️ by Leena Jain**
