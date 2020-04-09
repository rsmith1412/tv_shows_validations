from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta, date

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        today = date.today()
        rel_date = date.fromisoformat(postData['rel_date'])
        print(type(rel_date), "_________", type(today))
        # rel_date = date.fromisoformat(postData['rel_date'])
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network must be at least 3 characters"
        if rel_date > today:
            errors["rel_date"] = "Release date must be before today"
        if postData['desc'] and len(postData['desc']) < 10:
            errors["desc"] = "Show description must be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField()
    rel_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    def __repr__(self):
        return f"Show: {self.title} ({self.rel_date})"