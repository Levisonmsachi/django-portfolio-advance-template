# Levvie-Livvie  
### Django Portfolio — Advanced Template

<p align="center">
  <img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/blob/main/Screenshot%202025-12-16%20130802.png" width="720" alt="Portfolio Preview">
</p>

<p align="center">
  <strong>A clean, database-driven portfolio website built with Django.</strong><br>
  Projects · Skills · About · Contact · Admin Dashboard
</p>

<p align="center">
  <a href="https://github.com/Levisonmsachi/django-portfolio-advance-template">Repository</a>
  ·
  <a href="#features">Features</a>
  ·
  <a href="#getting-started">Getting Started</a>
  ·
  <a href="#deployment">Deployment</a>
  ·
  <a href="#contact">Contact</a>
</p>

---

## Overview

**Levvie-Livvie Django Portfolio** is an advanced, production-ready Django template designed to help developers present their work professionally.

All major sections are **database-powered**, making updates easy through the Django Admin — no code changes required for content updates.

**Author:** Levvie-Livvie  
**Email:** levisonmsachi03@gmail.com

---

## Features

- Dynamic **Projects** showcase (title, description, tech stack, image URL)
- Structured **Skills** section with proficiency levels
- Professional **About Me** page (bio, focus areas, availability)
- Functional **Contact Form** with stored submissions
- Fully configured **Django Admin Dashboard**
- Clean, responsive templates with static assets
- Beginner-friendly yet production-scalable structure

---

## Built With

- **Python**
- **Django** (6.x)
- **SQLite** (default database)
- Django Templates (HTML)
- CSS (static files)

---

## Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/Levisonmsachi/django-portfolio-advance-template/main/docs/screenshots/home.png" width="700">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Levisonmsachi/django-portfolio-advance-template/main/docs/screenshots/projects.png" width="700">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Levisonmsachi/django-portfolio-advance-template/main/docs/screenshots/contact.png" width="700">
</p>

---

## Project Structure

```text
portfolio/
├─ main/                     # Core app
│  ├─ migrations/
│  ├─ static/main/css/
│  ├─ templates/main/
│  ├─ models.py              # Project, Skill, AboutMe, ContactMessage
│  ├─ views.py
│  └─ urls.py
├─ portfolio/                # Project configuration
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py / asgi.py
├─ db.sqlite3
└─ manage.py
Getting Started
1. Clone the repository
bash
Copy code
git clone https://github.com/Levisonmsachi/django-portfolio-advance-template.git
cd django-portfolio-advance-template
2. Create and activate a virtual environment
Windows (PowerShell):

powershell
Copy code
python -m venv .venv
.\.venv\Scripts\Activate.ps1
Windows (CMD):

bat
Copy code
python -m venv .venv
.\.venv\Scripts\activate
macOS / Linux:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
bash
Copy code
pip install django
(You can add requirements.txt later for convenience.)

4. Apply migrations
bash
Copy code
python manage.py migrate
5. Create an admin user
bash
Copy code
python manage.py createsuperuser
6. Run the development server
bash
Copy code
python manage.py runserver
Open in your browser:

Website: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

Admin Content Management
The Django Admin allows you to manage:

Projects

Skills

About Me content

Contact messages

All portfolio updates can be done without touching code.

Configuration Notes
Default settings:

DEBUG = True

SQLite database

Empty ALLOWED_HOSTS

For production:

Set DEBUG = False

Configure ALLOWED_HOSTS

Store SECRET_KEY in environment variables

Run collectstatic

Deployment
This project can be deployed to:

Render

Railway

Fly.io

Heroku

VPS (Gunicorn + Nginx)

Typical flow:

bash
Copy code
python manage.py migrate
python manage.py collectstatic
gunicorn portfolio.wsgi
Roadmap
 Add requirements.txt

 Environment variable support (.env)

 Media uploads for project images

 Automated tests

 Theme customization options

Contact
Levvie-Livvie
📧 levisonmsachi03@gmail.com


