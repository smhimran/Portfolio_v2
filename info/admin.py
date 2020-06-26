from django.contrib import admin
from .models import Education, Project, job, Extracurricular, music

# Register your models here.
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(job)
admin.site.register(Extracurricular)
admin.site.register(music)
