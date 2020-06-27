from django.shortcuts import render
from .models import Education, Project, job, Extracurricular, music

# Create your views here.
def index(request):
    edu = Education.objects.all()
    top = Project.objects.all()[:1].get()
    latest = None
    other = Project.objects.all()[1:]
    jobs = job.objects.all()
    extra = Extracurricular.objects.all()
    mus = music.objects.all()[:4]

    context = {'edu': edu, 'top': top, 'latest': latest, 'other': other, 'jobs': jobs,
               'extra': extra, 'music': mus
               }

    return render(request, 'info/index.html', context)

def resume(request):
    edu = Education.objects.all()[:1]
    projects = Project.objects.all()
    jobs = job.objects.all()
    extra = Extracurricular.objects.all()[1:2]

    context = {'edu': edu, 'projects': projects, 'jobs': jobs, 'extra': extra}

    return render(request, 'info/resume.html', context)