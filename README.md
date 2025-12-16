<p align="center">
  <img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/raw/main/Screenshot%202025-12-16%20130802.png" width="800" alt="Levvie-Livvie Portfolio Dashboard">
</p>

<h1 align="center">🚀 Levvie-Livvie Portfolio</h1>
<h3 align="center">Advanced Django-Powered Portfolio System</h3>

<p align="center">
  <strong>A fully dynamic, database-driven portfolio template built with Django</strong><br>
  Professional • Scalable • Production-Ready
</p>

<p align="center">
  <a href="https://github.com/Levisonmsachi/django-portfolio-advance-template/stargazers">
    <img src="https://img.shields.io/github/stars/Levisonmsachi/django-portfolio-advance-template?style=for-the-badge&color=4CC9F0" alt="Stars">
  </a>
  <a href="https://github.com/Levisonmsachi/django-portfolio-advance-template/network/members">
    <img src="https://img.shields.io/github/forks/Levisonmsachi/django-portfolio-advance-template?style=for-the-badge&color=4361EE" alt="Forks">
  </a>
  <a href="https://github.com/Levisonmsachi/django-portfolio-advance-template/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-teal?style=for-the-badge" alt="License">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10+-306998?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-6.0+-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  </a>
</p>

<p align="center">
  <a href="#-key-features">Features</a> •
  <a href="#-live-preview">Preview</a> •
  <a href="#-quick-start">Installation</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-contact--connect">Contact</a>
</p>

<div align="center">
  <img src="https://img.shields.io/badge/DYNAMIC_CONTENT-7209B7?style=flat-square">
  <img src="https://img.shields.io/badge/ADMIN_DASHBOARD-3A0CA3?style=flat-square">
  <img src="https://img.shields.io/badge/FULLY_RESPONSIVE-4CC9F0?style=flat-square">
  <img src="https://img.shields.io/badge/PRODUCTION_READY-F72585?style=flat-square">
</div>

---

## ✨ Key Features

### 🎯 Core Capabilities
- Dynamic content management via Django models
- Zero-code updates using Django Admin
- Clean, modern, production-ready UI

### 📊 Portfolio Modules

| Module | Description | Admin |
|------|------------|-------|
| Projects | Showcase projects with images & stacks | ✅ |
| Skills | Visual proficiency matrix | ✅ |
| About | Bio, focus areas, availability | ✅ |
| Contact | Message storage system | ✅ |

### 🛠 Technical Excellence
- Django best-practice architecture
- Scalable DB (SQLite / PostgreSQL / MySQL)
- Secure defaults
- REST-API ready

---

## 📸 Live Preview

<div align="center">

<img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/raw/main/Screenshot%202025-12-16%20120823.png" width="90%">

<br><br>

<img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/raw/main/Screenshot%202025-12-16%20130743.png" width="45%">
<img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/raw/main/Screenshot%202025-12-16%20120847.png" width="45%">

</div>

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip
- Git

### Installation

```bash
git clone https://github.com/Levisonmsachi/django-portfolio-advance-template.git
cd django-portfolio-advance-template

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Access**
- Portfolio: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

---

## 🏗 Architecture

```text
django-portfolio-advance-template/
├── portfolio/
├── main/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── db.sqlite3
├── manage.py
└── README.md
```

### Core Models
```python
Project(title, description, tech_stack, image, created)
Skill(name, category, proficiency)
AboutMe(bio, availability, resume)
ContactMessage(name, email, message, timestamp)
```

---

## 🚢 Deployment

```bash
DEBUG=False
SECRET_KEY=your_secret
ALLOWED_HOSTS=yourdomain.com
python manage.py collectstatic
```

Supports:
- Render
- Railway
- Heroku
- VPS
- AWS EB

---

## 📈 Roadmap
- Blog Module
- Dark / Light Mode
- REST API
- Docker
- Analytics
- Multi-language support

---

## 🛡 Support

| Issue | Fix |
|-----|-----|
| Port busy | `python manage.py runserver 8080` |
| Migration error | Re-migrate DB |
| Static missing | collectstatic |

---

## 📞 Contact & Connect

<div align="center">

<strong>Levvie-Livvie</strong><br>
Full Stack Developer · Django Specialist

<br>

<a href="mailto:levisonmsachi03@gmail.com">
  <img src="https://img.shields.io/badge/Email-levisonmsachi03@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white">
</a>

<a href="https://github.com/Levisonmsachi">
  <img src="https://img.shields.io/badge/GitHub-Levisonmsachi-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

</div>

---

## 🌟 Show Your Support

<div align="center">
  <img src="https://img.shields.io/github/stars/Levisonmsachi/django-portfolio-advance-template?style=for-the-badge">
</div>

---

<p align="center">
  <sub>✨ Crafted with precision by <strong>Levvie-Livvie</strong> · December 2025 ✨</sub>
</p>
