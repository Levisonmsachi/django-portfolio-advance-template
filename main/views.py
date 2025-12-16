from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from . models import Project, Skills, AboutMe, ContactInfo, ContactMessage
from django.db import models
from django.contrib import messages

# View function for home page
def home(request):
    # Get recent projects
    recent_projects = Project.objects.filter(
        is_published=True
    ).order_by('-created_at')[:3]
    
    # Get statistics
    total_projects = Project.objects.filter(is_published=True).count()
    published_projects = Project.objects.filter(is_published=True).count()
    
    # Get unique technologies count
    technologies_used = Project.objects.filter(
        is_published=True
    ).values_list('technology', flat=True).distinct()
    
    all_technologies = set()
    for tech_string in technologies_used:
        if tech_string:
            tech_list = [tech.strip() for tech in tech_string.split(',')]
            all_technologies.update(tech_list)
    
    technologies_count = len(all_technologies)
    
    # Get top skills
    top_skills = Skills.objects.all().order_by('-proficiency')[:6]
    skills_count = Skills.objects.count()
    
    context = {
        'welcome_message': 'Welcome to My Portfolio',
        'recent_projects': recent_projects,
        'total_projects': total_projects,
        'published_projects': published_projects,
        'technologies': sorted(all_technologies),
        'technologies_count': technologies_count,
        'top_skills': top_skills,
        'skills_count': skills_count,
    }
    return render(request, 'main/home.html', context)



def about(request):
    try:
        about_data = AboutMe.objects.first()
    except AboutMe.DoesNotExist:
        about_data = None
    
    focus_areas_list = []
    if about_data and about_data.focus_areas:
        focus_areas_list = [area.strip() for area in about_data.focus_areas.split(',')]
    
    recent_projects = Project.objects.filter(is_published=True).order_by('-created_at')[:3]
    
    context = {
        'about': about_data,
        'focus_areas': focus_areas_list,
        'recent_projects': recent_projects,
    }
    return render(request, 'main/about.html', context)


# View function for projects page
def projects(request):
    # Get ALL published projects from database
    all_projects = Project.objects.filter(is_published=True)
    
    # Get unique technologies for filtering
    technologies = Project.objects.values_list(
        'technology', flat=True
    ).distinct()
    
    # Filter by technology if user selected one
    selected_tech = request.GET.get('tech')
    if selected_tech:
        all_projects = all_projects.filter(technology__icontains=selected_tech)
    
    # Pass data to template
    context = {
        'projects': all_projects,  # Now from database!
        'technologies': technologies,
        'selected_tech': selected_tech,
        'total_count': all_projects.count(),
    }
    return render(request, 'main/projects.html', context)

# View function for single project detail page
def project_detail(request, project_id):
    # Get project from database, or show 404 if not found
    project = get_object_or_404(Project, id=project_id, is_published=True)
    
    # Get related projects (same technology)
    related_projects = Project.objects.filter(
        technology__icontains=project.technology,
        is_published=True
    ).exclude(id=project.id)[:3]  # Exclude current project, limit to 3
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'main/project_detail.html', context)


def contact(request):
    contact_info = ContactInfo.objects.first()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, '✅ Message sent successfully! Thank you for reaching out. I\'ll get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, '❌ Please fill out all fields.')
    
    context = {
        'contact_info': contact_info,
    }
    return render(request, 'main/contact.html', context)



# View function for skills page
def skills(request):
    """View function for skills page"""
    # Get all skills from database, ordered by proficiency
    skills_list = Skills.objects.all().order_by('-proficiency')
    
    # Calculate statistics
    total_skills = skills_list.count()
    average_proficiency = skills_list.aggregate(models.Avg('proficiency'))['proficiency__avg']
    
    # Group skills by proficiency level
    expert_skills = skills_list.filter(proficiency__gte=80)
    intermediate_skills = skills_list.filter(proficiency__range=(60, 79))
    beginner_skills = skills_list.filter(proficiency__lt=60)
    
    # Also get technologies from projects
    technologies_used = Project.objects.filter(
        is_published=True
    ).values_list('technology', flat=True).distinct()
    
    all_technologies = set()
    for tech_string in technologies_used:
        if tech_string:
            tech_list = [tech.strip() for tech in tech_string.split(',')]
            all_technologies.update(tech_list)
    
    context = {
        'skills': skills_list,
        'technologies': sorted(all_technologies),
        'total_skills': total_skills,
        'average_proficiency': round(average_proficiency or 0, 1),
        'expert_skills': expert_skills,
        'intermediate_skills': intermediate_skills,
        'beginner_skills': beginner_skills,
        'expert_count': expert_skills.count(),
        'intermediate_count': intermediate_skills.count(),
        'beginner_count': beginner_skills.count(),
    }
    return render(request, 'main/skills.html', context)


# Custom 404 error handler
def custom_404(request, exception):
    """ Custom 404 error handler """
    return render(request, 'main/404.html', status=404)