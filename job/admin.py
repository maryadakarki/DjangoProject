from django.contrib import admin

from job.models import Category, Job

# Register your models here.
admin.site.register(Category)
admin.site.register(Job)