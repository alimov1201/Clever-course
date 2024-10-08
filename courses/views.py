from django.shortcuts import render, get_object_or_404
from courses.models import Course, Teachers

def course_page(request):
    category = request.GET.get('category')
    if category:
        courses = Course.objects.filter(category__profession__name__icontains=category)
    else:
        courses = Course.objects.all()
    context = {
        'courses': courses,
        'category': category
    }
    return render(request, 'courses.html', context=context)

def single_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.user.is_authenticated and request.user not in course.users.all():
        course.views += 1
        course.users.add(request.user)
        course.save()
    context = {
        'course': course
    }
    return render(request, 'single-course.html', context=context)

def search_course(request):
    search = request.GET.get('search')
    courses = Course.objects.filter(title__icontains=search)
    context = {
        'courses': courses,
        'search': search
    }
    return render(request, 'search-course.html', context=context)

def teacher(request):
    teachers = Teachers.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, 'instructors.html', context=context)
