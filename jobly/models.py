from django.db import models
from account.models import Account

import datetime
# Create your models here.
class Job(models.Model):
    STATUS_CHOICES = [
        ("AP", "Applied"),
        ("AC", "Accepted"),
        ("ASG", "Assignment Given"),
        ("RJ", "Rejected"),
        ("AD", "Assignment Done"),
        ("IV", "Interview"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_applied = models.DateField(default=datetime.date.today) 
    company = models.CharField(max_length=200)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default="AP",
    )
    job_url = models.URLField()
    posted_by = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="jobs"
    )

    def __str__(self):
        return self.title
