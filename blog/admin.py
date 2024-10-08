from django.contrib import admin

from blog.models import Blog, Upcoming_event, Contact, Comment

admin.site.register(Blog)
admin.site.register(Upcoming_event)
admin.site.register(Comment)
admin.site.register(Contact)
