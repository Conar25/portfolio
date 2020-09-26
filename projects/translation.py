from modeltranslation.translator import register, TranslationOptions

from .models import ProjectModel

@register(ProjectModel)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
