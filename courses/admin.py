from django.contrib import admin
 
from courses.models import Course, Course_category, Course_register, Teachers

admin.site.register(Course)
admin.site.register(Course_category)
admin.site.register(Course_register)
admin.site.register(Teachers)
