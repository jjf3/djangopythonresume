from django.shortcuts import render

# Create your views here.
from .models import Resume

def resume(request):
    resume = Resume.objects.first()  # Assuming you have only one resume instance
    return render(request, 'resume.html', {'resume': resume})