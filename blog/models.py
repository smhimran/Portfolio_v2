from django.db import models
from martor.models import MartorField
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(null=True, blank=True)
    banner = models.CharField(max_length=1000, default='https://i.ibb.co/kDcGv5D/sb-blog-programming.jpg')
    content = MartorField()
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:200]