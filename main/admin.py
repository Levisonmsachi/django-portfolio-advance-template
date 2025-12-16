from django.contrib import admin
from .models import Project, Skills, AboutMe, ContactInfo, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'description', 'technology')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'technology')
        }),
        ('Media', {
            'fields': ('image_url',)
        }),
        ('Status', {
            'fields': ('is_published',)
        }),
    )

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    list_filter = ('proficiency',)
    search_fields = ('name',)
    ordering = ('-proficiency',)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'years_of_experience', 'availability', 'updated_at')
    fieldsets = (
        ('Profile Information', {
            'fields': ('title', 'bio', 'professional_summary')
        }),
        ('Experience & Focus', {
            'fields': ('years_of_experience', 'focus_areas')
        }),
        ('Contact Information', {
            'fields': ('email', 'location', 'availability')
        }),
    )
    readonly_fields = ('updated_at',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone', 'updated_at')
    fieldsets = (
        ('Contact Details', {
            'fields': ('title', 'description', 'email', 'phone', 'location')
        }),
        ('Availability', {
            'fields': ('availability_message', 'response_time')
        }),
        ('Social Links', {
            'fields': ('social_links',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('updated_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'name', 'email', 'subject', 'message')
    
    fieldsets = (
        ('Message Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
