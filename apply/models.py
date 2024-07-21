from datetime import datetime
from django.db import models
from job.models import Job

from account.models import User


class Apply(models.Model):
    # Other fields in your model...
    job = models.ForeignKey(Job, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    checkbox = models.BooleanField(default=False)
    jobapplied_at = models.DateField(default=datetime.now,blank=True)

    def save(self, *args, **kwargs):
        if not self.checkbox:
            # Handle case where terms are not accepted
            raise ValueError("You must accept the terms and conditions")
        super(Apply, self).save(*args, **kwargs)