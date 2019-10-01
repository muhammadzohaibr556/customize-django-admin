from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def report(request):
    return render (request,"report.html")