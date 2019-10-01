from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Report(TemplateView):
    template_name = 'report.html'