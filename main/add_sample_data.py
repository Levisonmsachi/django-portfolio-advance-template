# add_sample_data.py
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Project

# Clear existing data
Project.objects.all().delete()

# Sample projects
sample_projects = [
    {
        'title': 'Portfolio Website',
        'description': 'A personal portfolio website built with Django to showcase my projects and skills. Features include project filtering, search functionality, and a responsive design.',
        'technology': 'Django, HTML, CSS, JavaScript, SQLite',
        'is_published': True,
    },
    {
        'title': 'E-commerce Platform',
        'description': 'Full-featured online store with user authentication, product catalog, shopping cart, and Stripe payment integration. Includes admin dashboard for inventory management.',
        'technology': 'Django, React, Stripe API, PostgreSQL',
        'is_published': True,
    },
    {
        'title': 'Blog Application',
        'description': 'Multi-user blog platform with rich text editing, comments, categories, and user profiles. Includes markdown support and image uploads.',
        'technology': 'Django, Bootstrap, PostgreSQL, Markdown',
        'is_published': True,
    },
    {
        'title': 'Task Manager',
        'description': 'Todo list application with drag-and-drop functionality, due dates, priority levels, and progress tracking. Supports team collaboration.',
        'technology': 'Python, Flask, SQLite, JavaScript',
        'is_published': True,
    },
    {
        'title': 'Weather Dashboard',
        'description': 'Real-time weather application showing forecasts, historical data, and weather alerts. Integrates with multiple weather APIs.',
        'technology': 'Django, REST API, Chart.js, Redis',
        'is_published': True,
    },
    {
        'title': 'Recipe Sharing Platform',
        'description': 'Community-driven recipe sharing website with user ratings, meal planning, and grocery list generation. Includes dietary filter options.',
        'technology': 'Django, HTML, CSS, JavaScript',
        'is_published': True,
    },
    {
        'title': 'Learning Management System',
        'description': 'Online course platform with video lessons, quizzes, progress tracking, and certificate generation. Supports instructor dashboards.',
        'technology': 'Django, Video.js, PostgreSQL',
        'is_published': False,  # This one is not published
    },
]

# Add to database
for data in sample_projects:
    Project.objects.create(**data)

print(f"Added {len(sample_projects)} sample projects to database!")