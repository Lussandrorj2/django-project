from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title', 'user__username')
    list_filter = ('user',)

admin.site.register(Project, ProjectAdmin)

# Register your models here.
