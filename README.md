# djangopythonresume
My resume created using python and django
1. I already had python and django installed so first step would be django-admin startproject myresume
2. cd myresume
3. python manage.py startapp resumeapp
Replace the settings.py, models.py, views.py, and urls.py files in the myresume directory with the code provided below:
# settings.py
...
<INSTALLED_APPS = [
    ...
    'resumeapp',
]
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.request',
            ],
        },
    },
]
...>

# models.py
from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()

# views.py
from django.shortcuts import render
from .models import Resume

def resume(request):
    resume = Resume.objects.first()  # Assuming you have only one resume instance
    return render(request, 'resume.html', {'resume': resume})

# urls.py
from django.contrib import admin
from django.urls import path
from resumeapp.views import resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', resume, name='resume'),
]

4. Create a new directory called templates inside the resumeapp directory.
5. Inside the templates directory, create a new HTML file named resume.html with the following code:
<!DOCTYPE html>
<html>
<head>
    <title>My Resume</title>
</head>
<body>
    <h1>{{ resume.name }}</h1>
    <p>Email: {{ resume.email }}</p>
    <p>Phone: {{ resume.phone }}</p>

    <h2>Summary</h2>
    <p>{{ resume.summary }}</p>

    <h2>Education</h2>
    <p>{{ resume.education }}</p>

    <h2>Experience</h2>
    <p>{{ resume.experience }}</p>

    <h2>Skills</h2>
    <p>{{ resume.skills }}</p>
</body>
</html>
6. Apply Database Migrations: python manage.py migrate
7. Create a superuser to access the Django admin: python manage.py createsuperuser
8. launch server python manage.py runserver
9. use localhost:8000/MyResume to access resume and /admin to login to django admin center. 
10. If error in admin center please add the following code to admin.py: 
from .models import Resume

admin.site.register(Resume)
11.  You must set settings.ALLOWED_HOSTS if DEBUG is False.
12.  Then you can see your resume at localhost:8000/resume/


