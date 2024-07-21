from datetime import datetime

from django.db import models
from account.models import User
from job.models import Category


# Create your models here.
class Pro(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    pro_name = models.CharField(max_length=150)
    pro_bio = models.CharField(max_length=150)
    pro_dob = models.DateField(default=datetime.now, blank=True)
    pro_pic = models.ImageField(upload_to='pro_image/')
    pro_number = models.CharField(null=True, max_length=10)
    pro_cv = models.FileField(upload_to='pdfs/')
    pro_certificates = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.user
