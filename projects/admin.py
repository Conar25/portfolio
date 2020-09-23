from django.contrib import admin

from .models import ProjectModel

@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        ordering: ['-created_date']
