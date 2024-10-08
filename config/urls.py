"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog.views import blog, blog_detail, main, contact
from register.views import user_login, register, user_logout
from courses.views import course_page, single_course, teacher, search_course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='home'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('teacher/', teacher, name='teacher'),
    path('course/', course_page, name='course'),
    path('search_course/', search_course, name='search_course'),
    path('blog-detail/<int:id>', blog_detail, name='blog_detail'),
    path('single-course/<int:id>/', single_course, name='single_course')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

