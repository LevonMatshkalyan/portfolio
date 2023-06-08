from django.shortcuts import render , get_object_or_404

from .models import Job , CV

# Create your views here.

def home(request):
    jobs = Job.objects
    cv = CV.objects.get(pk=1)

    return render(request , 'jobs/home.html',{'jobs':jobs,
                                              'cv':cv})

def detail(request , job_id):
    job_detail = get_object_or_404(Job , pk = job_id)
    return render(request ,'jobs/detail.html' , { 'job' : job_detail})

