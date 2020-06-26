from django.db import models

# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start = models.CharField(max_length=10)
    present = models.BooleanField(blank=True, null=True, default=False)
    end = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.degree


class Project(models.Model):
    title = models.CharField(max_length=500)
    summary = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='info/images/Projects',blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title

class job(models.Model):
    designation = models.CharField(max_length=200)
    institution = models.CharField(max_length=300)
    start = models.CharField(max_length=10)
    present = models.BooleanField(blank=True, null=True, default=False)
    end = models.CharField(max_length=10, blank=True, null=True)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.institution

class Extracurricular(models.Model):
    designation = models.CharField(max_length=200)
    institution = models.CharField(max_length=300)
    start = models.CharField(max_length=10)
    present = models.BooleanField(blank=True, null=True, default=False)
    end = models.CharField(max_length=10, blank=True, null=True)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.institution

class music(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name