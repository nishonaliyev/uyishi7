from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_entry = models.CharField(max_length=30)
    title_description = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now_add=timezone.now())
    body = models.TextField()

    def __str__(self) -> str:
        return self.title_description

class Media(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
