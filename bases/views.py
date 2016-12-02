from django.shortcuts import render, get_object_or_404,redirect
from .models import Bailarines,Instructor_danza
from .forms import Bailarines_form
from .forms import Instructores_form
from .forms import Consulta_form
from .forms import Ingresar
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.views.generic import UpdateView
from .models import Trainer
from .forms import Trainer_form
from django.db import models
from django.urls import reverse
# Create your views here.
def bailarines_list(request):
	b = Bailarines.manager.all ()
	form = Bailarines_form(request.POST or None)
	return render (request, 'bailarines_list.html', {'list' :b, 'form' :form})

class Bailarines_register_view(TemplateView):
	template_name = 'bailarines_register.html'

class Instructores_register_view(TemplateView):
	template_name = 'instructores_register.html'
	
class Index_view(TemplateView):
	template_name = 'index.html'	

def instructores_list(request):
	i = Instructor_danza.objects.all ()
	form = Instructores_form(request.POST or None)
	return render (request, 'instructores_list.html', {'list' :i, 'form' :form})

def bailarines_register(request):
	form = Bailarines_form(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			b_name = form.cleaned_data['nombre_bailarin']
			b_apellidop = form.cleaned_data['apellido_paterno_bailarin']
			b_apellidom = form.cleaned_data['apellido_materno_bailarin']
			b_edad = form.cleaned_data['edad_bailarin']
			b_curso = form.cleaned_data['curso']
			b_horario = form.cleaned_data['horario_ensayo']
			b_image = form.cleaned_data['image_bailarin']

		
			Bailarines.manager.create(nombre_bailarin=b_name,apellido_paterno_bailarin=b_apellidop,apellido_materno_bailarin=b_apellidom,edad_bailarin= b_edad,curso=b_curso,horario_ensayo=b_horario,image_bailarin=b_image)


		return HttpResponseRedirect('/')
	else:
		form = Bailarines_form()
	ctx={'form':form}
	return render(request,'bailarines_register.html', ctx)

def instructores_register(request):
	form = Instructores_form(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			i_name = form.cleaned_data['nombre']
			i_apellidop = form.cleaned_data['apellido_paterno']
			i_apellidom = form.cleaned_data['apellido_materno']
			i_edad = form.cleaned_data['edad']
			i_especialidad = form.cleaned_data['especialidad']
			i_horario = form.cleaned_data['horario_trabajo']
			i_image = form.cleaned_data['image_ins']

		
			Instructor_danza.objects.create(nombre=i_name,apellido_paterno=i_apellidop,apellido_materno=i_apellidom,edad=i_edad,especialidad=i_especialidad,horario_trabajo=i_horario, image_ins=i_image)

		

		return HttpResponseRedirect('/')
	else:
		form = Instructores_form()
	ctx={'form':form}
	return render(request,'instructores_register.html', ctx)







		#form = Ingresar(request.POST)
		#if form.is_valid():
		#	return HttpResponseRedirect(reverse('Bailarines_Detail_view', args=(=)))
		#else:
		#	form = Ingresar()
		#	return render(request,'au.html', {'form': form})





class Register_Bailarines(CreateView):
	template_name ='bailarines_register.html'
	model = Bailarines
	fields = '__all__'
	success_url = reverse_lazy('Index_view')

class Register_Instructores(CreateView):
	template_name ='instructores_register.html'
	model = Instructor_danza
	fields = '__all__'
	success_url = reverse_lazy('Index_view')
class Sigup(FormView):
	template_name = 'sigup.html'
	form_class = Trainer_form
	#fields = ['trainer_perfil', 'mail', 'phone']
	success_url = reverse_lazy('Index_view')

	def form_valid(self, form):
		user = form.save()
		p = Trainer()
		p.trainer_perfil = user
		p.mail = form.cleaned_data['mail']
		p.phone = form.cleaned_data['phone']
		p.save()
		return super(Sigup, self).form_valid(form)
def consulta (request):
	i = Instructor_danza.objects.all()
	form = Consulta_form(request.POST or None)
	return render (request, 'consultas.html', {'list' :i, 'form' :form})
def consulta2 (request):
	b = "Brenda"
	a = Instructor_danza.objects.order_by(nombre=b)
	form = Consulta_form(request.POST or None)
	return render (request, 'consulta2.html', {'list' :a, 'form' :form})
def consulta3 (request):
	c = 1
	#b = Instructor_danza.objects.filter(pk= c)
	#form = Consulta_form(request.POST or None)
	#return render (request, 'consulta3.html', {'list' :b, 'form' :form}) 
	return HttpResponseRedirect(reverse('Bailarines_Detail_view', args=(c,)))
def consulta4 (request):
	c = Instructor_danza.objects.filter(especialidad="Pandero").order_by('nombre')
	form = Consulta_form(request.POST or None)
	return render (request, 'consulta4.html', {'list' :c, 'form' :form}) 
class auxiliar(TemplateView):
	template_name = 'auxiliarconsu.html'

class imagenes(TemplateView):
	template_name = 'imagen.html'

class Bailarines_Detail(DetailView):
	template_name = 'bailarines_detail.html'
	model = Bailarines

def buscar_bailarines(request):
	if request.method == 'POST':
		try:
			buscar_id = request.POST.get('bailarines_input', None)
			q = Bailarines.manager.get(id = buscar_id)
			return render(request, 'nodetalle.html', {'list':q})
		except Bailarines.DoesNotExist: 
			return HttpResponseRedirect("Bailarin no encontrado")
class bailarines_report(ListView):
	template_name = 'bailarines_report.html'
	model = Bailarines

class Update_bailarines(UpdateView):
	model = Bailarines
	fields ='__all__'
	template_name = 'update_bailarin.html'
	success_url = reverse_lazy('bailarines_report_view')
class Detail_Trainer(DetailView):
	template_name= 'detail_trainer.html'
	model = Instructor_danza
def Bailarines_update(request, pk, template_name= 'update_bailarin.html'):
	bailarin = get_object_or_404(Bailarines, pk=pk)
	form = Bailarines_form(request.POST or None, instance=bailarin)
	if form.is_valid():
		form.save()
		return redirect ('bailarines_report_view')
	return render (request, template_name, {'form': form})

