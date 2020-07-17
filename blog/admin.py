from django.contrib import admin
from django.db import models
from .models import Post
from martor.widgets import AdminMartorWidget
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Post, PostAdmin)