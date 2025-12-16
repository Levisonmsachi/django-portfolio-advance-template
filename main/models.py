from django.db import models

class Project(models.Model):
    # Each field represents a database column
    title = models.CharField(max_length=200)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    title = models.CharField(max_length=200)
    bio = models.TextField()
    professional_summary = models.TextField()
    years_of_experience = models.IntegerField(default=0)
    focus_areas = models.TextField(help_text="Comma-separated focus areas")
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    availability = models.CharField(max_length=100, default="Available for projects")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"


class ContactInfo(models.Model):
    title = models.CharField(max_length=200, default="Get In Touch")
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    response_time = models.CharField(max_length=100, default="Within 24 hours")
    social_links = models.TextField(blank=True, help_text="JSON format or comma-separated key:value pairs")
    availability_message = models.CharField(max_length=255, default="I'd love to hear from you!")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']