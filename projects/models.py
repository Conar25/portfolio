import os

from django.db import models
from django.contrib.staticfiles import finders

from taggit.managers import TaggableManager

class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,
                            db_index=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    def get_image(self):
        valid_extensions = ['jpg', 'png', 'gif']
        for extension in valid_extensions:
            path = os.path.join('img', 'projects' ,self.slug + '.' + extension)
            if finders.find(path):
                return path
                
        return 'img/projects/default.png'

    def get_template(self):
        return os.path.join('projects', self.slug + '.html')
    
    def __str__(self):
        return self.title
