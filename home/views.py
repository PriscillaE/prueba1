from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class About_view(TemplateView):
	template_name = 'about.html'