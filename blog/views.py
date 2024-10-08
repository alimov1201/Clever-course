from tokenize import Comment
from django.shortcuts import render, get_object_or_404
from courses.forms import Register_form
from courses.models import Course_category, Course, Teachers
from blog.forms import ContactForm, CommentForm
from blog.models import Blog, Upcoming_event, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def blog(request):
    courses = Course.objects.all()
    categories = Course_category.objects.all()
    paginator = Paginator(courses, 2)
    page_num = request.GET.get('page')
    if not page_num:
        page_num = 1  
    pages = paginator.num_pages
    if int(page_num) > pages or int(page_num) < 1:
        page_num = 1
    page_obj = paginator.get_page(page_num)
    context = {
        'categories': categories,
        'courses': courses,
        'page_obj': page_obj,
        'page_num': page_num
    }
    return render(request, 'blog.html', context=context)

def blog_detail(request, id):
    articles = get_object_or_404(Blog, id=id)
    comments = Comment.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.user.username
            comment.article = articles
            comment.save()
    context = {
        'article': articles,
        'form': form,
        'comments': comments
    }
    return render(request, 'blog-details.html', context=context)

def main(request):
    articles = Blog.objects.order_by('-id')[:2]
    courses = Course.objects.order_by('-users')[:3]
    events = Upcoming_event.objects.order_by('-id')[:3]
    article_count = Blog.objects.count()
    user_count = User.objects.count()
    course_count = Course.objects.count()
    teacher_count = Teachers.objects.count()
    form = Register_form()
    if request.method == "POST":
        form  = Register_form(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'courses': courses,
        'articles': articles,
        'article_count': article_count,
        'user_count': user_count,
        'course_count': course_count,
        'teacher_count': teacher_count,
        'events': events,

    }
    return render(request, 'index.html', context=context)

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context=context)