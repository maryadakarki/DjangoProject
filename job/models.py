from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, FileExtensionValidator

from account.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.created_at)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    job_title = models.CharField(max_length=150)
    job_description = models.TextField()
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_validity = models.DateField(default=datetime.now, blank=True)
    job_created_at = models.DateTimeField(auto_now_add=True)
    job_updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.job_title, self.job_created_at)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.job_title

    class Meta:
        db_table = 'job'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'





