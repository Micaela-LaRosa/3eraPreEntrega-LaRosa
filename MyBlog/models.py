from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    publish_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    modified_date = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return f"title: {self.title}, about: {self.text}, publish on: {self.publish_date}"
    
class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment=True
        self.save()
    
    def __str__(self):
        return f"Comment from {self.author}, created {self.created_date}, consists on: {self.text}"
    
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"The user {self.name} {self.last_name} email contact is: {self.email}"