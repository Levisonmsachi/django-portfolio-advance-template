from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  # Home page (empty path)
    path('about/', views.about, name='about'),  # About page
    path('projects/', views.projects, name='projects'),  # Projects page
    path('projects/<int:project_id>/', views.project_detail, name='project-detail'),  # Project detail page
    path('skills/', views.skills, name='skills'), # Skills page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('404/', views.custom_404, name='custom-404'), # Custom 404 page for testing
]