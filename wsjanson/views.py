from django.shortcuts import render

# Create your views here.
from bases.models import Bailarines
from bases.models import Instructor_danza
from django.core import serializers
from django.http import HttpResponse

def wsBailarines(request):
	data= serializers.serialize('json', Bailarines.manager.all()) 
	return HttpResponse(data, content_type='application/json')

def xmBailarines(request):
	data= serializers.serialize('xml', Bailarines.manager.all()) 
	return HttpResponse(data, content_type='application/xml')

def wsInstructor_danza(resquest):
	data= serializers.serialize('json', Instructor_danza.objects.all())
	return HttpResponse(data, content_type='application/json')