from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BailarinesQuerySet(models.QuerySet):
	def pandero_curso(self, cursos):
		return self.filter(curso=cursos)

	def  nombre_bailarin(self):
		return self.order_by('nombre_bailarin')
	
	def  edad_bailarin(self,edad):
		return self.filter(edad_bailarin__lt=edad)
	
class Bailarines(models.Model):
	nombre_bailarin = models.CharField(max_length=20)
	apellido_paterno_bailarin = models.CharField(max_length=20)
	apellido_materno_bailarin = models.CharField(max_length=20)
	edad_bailarin = models.IntegerField()
	curso = models.CharField(max_length=25)
	horario_ensayo = models.CharField(max_length=10)
	image_bailarin = models.ImageField(upload_to='Bailarines_Image', blank=True)
	Instructor_danza = models.CharField(max_length=60)
	id = models.IntegerField(primary_key=True)
	#slug = models.SlugField()

	manager= BailarinesQuerySet.as_manager()

	def __unicode__(self):
		return "Nombre: %s - Apellido: %s - Edad: %s"%(self.nombre_bailarin,self.apellido_paterno_bailarin,self.edad_bailarin)

	def curso_pandero(self):
		if self.curso=='Banderas':
			return True
		else:
			return False
		curso_pandero.boolean=True
	
	curso_pandero.short_description='Nivel Avanzado'


class Instructor_danza(models.Model):
	nombre = models.CharField(max_length=20)
	apellido_paterno = models.CharField(max_length=20)
	apellido_materno = models.CharField(max_length=20)
	edad = models.FloatField()
	especialidad = models.CharField(max_length=25)
	horario_trabajo = models.CharField(max_length=10)
	image_ins = models.ImageField(upload_to='Ins_Image', blank=True)
	bailarin = models.ManyToManyField(Bailarines)
	id = models.IntegerField(primary_key=True)

	def __unicode__(self):
		return "Nombre: %s - Apellido: %s - Edad: %s"%(self.nombre,self.apellido_paterno,self.edad)

class Trainer(models.Model):
	trainer_perfil = models.OneToOneField(User)
	mail = models.EmailField()
	phone = models.IntegerField()
	

def __unicode__(self):
	return self.trainer_perfil.username
