from django.db import models
# Create your models here.
class Jobs(models.Model):

    job_title = models.CharField(max_length=225)
    job_discribtion = models.CharField(max_length=350)
    hourly_rate = models.FloatField()
    job_period = models.IntegerField()
    job_requirement = models.CharField(max_length=100)
    #username = models.ForeignKey(User, max_length=150)