from django.db import models
from django.contrib.auth.models import User

class Course_category(models.Model):
    name = models.CharField(max_length=100)
    back_image = models.ImageField(upload_to='category_back_image/')
    def __str__(self):
        return self.name
    

class Teachers(models.Model):
    image = models.ImageField(upload_to='teacher_image/')
    name = models.CharField(max_length=100)
    profession = models.ForeignKey(Course_category, on_delete=models.CASCADE, related_name='category')
    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_image/')
    category = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, related_name='teacher')
    price = models.PositiveIntegerField(null=True, blank=True)
    is_free = models.BooleanField(default=True)
    views = models.PositiveIntegerField()
    users = models.ManyToManyField(User, blank=True, related_name="account")
    def __str__(self):
        return self.title

class Course_register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
