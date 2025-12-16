<p align="center">
  <img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/blob/main/Screenshot%202025-12-16%20130802.png" width="800" alt="Levvie-Livvie Portfolio Dashboard">
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
    <img src="https://img.shields.io/badge/Python-3.10+-306998?style=for-the-badge&logo=python" alt="Python">
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-6.0+-092E20?style=for-the-badge&logo=django" alt="Django">
  </a>
</p>

<p align="center">
  <a href="#-key-features">Features</a> •
  <a href="#-live-preview">Preview</a> •
  <a href="#-quick-start">Installation</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-contact">Contact</a>
</p>

<div align="center">
  <img src="https://img.shields.io/badge/-DYNAMIC_CONTENT-7209B7?style=flat-square" alt="Dynamic">
  <img src="https://img.shields.io/badge/-ADMIN_DASHBOARD-3A0CA3?style=flat-square" alt="Admin">
  <img src="https://img.shields.io/badge/-FULLY_RESPONSIVE-4CC9F0?style=flat-square" alt="Responsive">
  <img src="https://img.shields.io/badge/-PRODUCTION_READY-F72585?style=flat-square" alt="Production">
</div>

---

## ✨ Key Features

### 🎯 **Core Capabilities**
- **Dynamic Content Management** - All portfolio sections powered by database models
- **Zero-Code Updates** - Modify content through Django Admin without touching code
- **Professional Presentation** - Clean, modern design with optimal UX/UI

### 📊 **Portfolio Modules**
| Module | Description | Admin Configurable |
|--------|-------------|-------------------|
| **Projects Showcase** | Display projects with images, descriptions, and tech stacks | ✅ |
| **Skills Dashboard** | Visual skill matrix with proficiency levels | ✅ |
| **About Me Section** | Professional bio, focus areas, and availability status | ✅ |
| **Contact System** | Functional contact form with message storage | ✅ |

### 🛠️ **Technical Excellence**
- **Modern Django Architecture** - Follows Django best practices
- **Scalable Database Design** - Ready for PostgreSQL, MySQL, or SQLite
- **Static Asset Optimization** - Organized CSS and template structure
- **Security Ready** - Built-in Django security features
- **REST API Ready** - Easy to extend with Django REST Framework

---

## 📸 Live Preview

<div align="center">
  
### 🖥️ Main Portfolio Interface
<img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/blob/main/Screenshot%202025-12-16%20120823.png" width="90%" alt="Portfolio Interface">
  
### 📱 Responsive Design
<img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/blob/main/Screenshot%202025-12-16%20130743.png" width="45%" style="margin-right: 2%;" alt="Mobile View">
<img src="https://github.com/Levisonmsachi/django-portfolio-advance-template/blob/main/Screenshot%202025-12-16%20120847.png" width="45%" alt="Admin Panel">

</div>

---

## 🚀 Quick Start

### **Prerequisites**
- Python 3.10 or higher
- pip (Python package manager)
- Git

### **Installation & Setup**

```bash
# 1. Clone the repository
git clone https://github.com/Levisonmsachi/django-portfolio-advance-template.git
cd django-portfolio-advance-template

# 2. Create and activate virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install django

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (for admin access)
python manage.py createsuperuser

# 6. Launch development server
python manage.py runserver
Access Points
🌐 Portfolio Website: http://127.0.0.1:8000/

⚙️ Admin Dashboard: http://127.0.0.1:8000/admin/

📧 Default Admin: Use credentials from createsuperuser step

🏗️ Architecture
Project Structure
text
django-portfolio-advance-template/
│
├── portfolio/                    # Project Configuration
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL routing
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── main/                        # Core Application
│   ├── migrations/              # Database migrations
│   ├── static/main/             # Static assets
│   │   ├── css/                 # Stylesheets
│   │   └── images/              # Static images
│   │
│   ├── templates/main/          # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── index.html           # Home page
│   │   ├── projects.html        # Projects showcase
│   │   ├── skills.html          # Skills display
│   │   ├── about.html           # About section
│   │   └── contact.html         # Contact form
│   │
│   ├── __init__.py
│   ├── admin.py                 # Admin configurations
│   ├── apps.py                  # App configuration
│   ├── models.py                # Database models
│   ├── views.py                 # Application views
│   ├── urls.py                  # App URL routing
│   └── tests.py                 # Test cases
│
├── db.sqlite3                   # Database (development)
├── manage.py                    # Django CLI
└── README.md                    # Documentation
Database Models
python
# Core Models Overview
- Project: title, description, tech_stack, image_url, date_created
- Skill: name, category, proficiency (1-100), icon_class
- AboutMe: bio, focus_areas, availability, resume_url
- ContactMessage: name, email, message, timestamp, is_read
⚙️ Admin Dashboard Guide
Accessing the Dashboard
Navigate to /admin

Login with superuser credentials

Manage all portfolio content through intuitive interfaces

Content Management
Section	Actions Available
Projects	Add, edit, delete, preview
Skills	Update proficiency, categories
About Me	Edit bio, availability status
Messages	View, mark as read, respond
Quick Updates
Change Bio: Main → AboutMe → Edit

Add Project: Main → Projects → Add

Update Skills: Main → Skills → Select and edit

🚢 Deployment
Platform Recommendations
Platform	Difficulty	Best For
Render	Easy	Quick deployment, free tier
Railway	Easy	Automatic deployments
Heroku	Medium	Traditional PaaS
VPS (DigitalOcean)	Advanced	Full control, scalable
AWS Elastic Beanstalk	Medium	AWS ecosystem
Production Checklist
bash
# 1. Set environment variables
DEBUG=False
SECRET_KEY=your_production_secret
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# 2. Collect static files
python manage.py collectstatic

# 3. Use production database
# Update settings.py with PostgreSQL/MySQL

# 4. Configure static files (WhiteNoise/NGINX)
# 5. Set up SSL certificate
# 6. Configure domain and DNS
Quick Render Deployment
Push code to GitHub repository

Create new Web Service on Render

Connect GitHub repository

Set build command: pip install django && python manage.py migrate

Set start command: gunicorn portfolio.wsgi:application

Add environment variables

Deploy!

📈 Roadmap
Next Features
Media Upload Integration - Cloudinary/AWS S3 support

Dark/Light Theme Toggle - User preference switching

Analytics Dashboard - Visitor insights and metrics

Blog Module - Integrated blogging system

API Endpoints - REST API for external integrations

Docker Support - Containerized deployment

Automated Testing - Comprehensive test suite

Multi-language Support - Internationalization (i18n)

Enhancements Planned
Email notifications for contact form

Project filtering and search

Skill progress animations

SEO optimization tools

Performance monitoring

🛡️ Support
Troubleshooting Common Issues
Issue	Solution
Port already in use	python manage.py runserver 8080
Migration errors	Delete db.sqlite3 and migration files, re-migrate
Static files not loading	Run python manage.py collectstatic
Admin access issues	Recreate superuser: python manage.py createsuperuser
Need Help?
Check existing GitHub Issues

Review Django documentation for framework-specific questions

Contact support for template-specific issues

📞 Contact & Connect
<div align="center">
Levvie-Livvie
Full Stack Developer & Django Specialist

https://img.shields.io/badge/Email-levisonmsachi03@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white
https://img.shields.io/badge/GitHub-Levisonmsachi-181717?style=for-the-badge&logo=github&logoColor=white
https://img.shields.io/badge/%F0%9F%96%A5%EF%B8%8F_Portfolio_Project-4CC9F0?style=for-the-badge&logo=google-chrome&logoColor=white

</div>
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

Permissions Include:

✅ Commercial use

✅ Modification

✅ Distribution

✅ Private use

Requirements:

📝 License and copyright notice preservation

<div align="center">
🌟 Show Your Support
If this project helped you, please give it a star!

https://img.shields.io/github/stars/Levisonmsachi/django-portfolio-advance-template?style=social&label=Star&maxAge=2592000

🎯 Built With Precision
https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white

✨ Crafted with passion by Levvie-Livvie • December 2025 ✨

</div>

