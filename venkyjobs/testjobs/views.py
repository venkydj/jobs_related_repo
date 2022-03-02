from django.shortcuts import render
from testjobs.models import Hyderabadjobs, Bangalorejobs,punejobs

# Create your views here.
def home_view(request):
    return render(request,'jobsapp/index.html')
def Hyderabad_view(request):
    jobs_list=Hyderabadjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/hyderabad.html',context=my_dict)

def Bangalorejobs_view(request):
    jobs_list=Bangalorejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/bangalore.html',context=my_dict)
def punejobs_view(request):
    jobs_list=punejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/pune.html',context=my_dict)
