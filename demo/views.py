from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import DemoProfile
# Create your views here.
@login_required
def report(request):
    demoProfile = DemoProfile.objects.raw('SELECT id, name, image FROM demo_demoprofile')
    args = {'profile':demoProfile}
    return render (request,"report.html",args)