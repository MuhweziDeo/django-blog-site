from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# import user table to access user


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now) 
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # deletes post if user is deleted

    def __str__(self):
        return self.title

    """redirect after a post is created"""
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

    