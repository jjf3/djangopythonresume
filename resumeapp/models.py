from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()