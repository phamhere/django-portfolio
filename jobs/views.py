from django.shortcuts import render

from .models import Job


def home(request):
    # get all the job objectss from the db and turn them into python objects
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
