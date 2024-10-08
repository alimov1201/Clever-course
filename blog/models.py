from django.db import models
from courses.models import Teachers
from django.core.exceptions import ValidationError
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    image = models.ImageField(upload_to='blog_image/')
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    title =  models.CharField(max_length=100)
    description = models.TextField()


def validate_future_datetime(value):
    if value <= timezone.now():
        raise ValidationError("The datetime must be in the future.")

class Upcoming_event(models.Model):
    image = models.ImageField(upload_to='event_image/')
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    event_datetime = models.DateTimeField(validators=[validate_future_datetime])

class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')