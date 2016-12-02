from django.contrib import admin

from .models import Instructor_danza
from .models import Bailarines
from .models import Trainer
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _ 
# Register your models here.
class CursoListFilter(admin.SimpleListFilter):
	title =_('curso activo')
	parameter_name = 'cursos'

	def lookups(self, request, model_admin):
		return(
			('Pandero4', _('Nivel Avanzado')),
			('Banderas', _('Fuerza')),
			('Tecnica Danza', _('Tecnica'))
		)
	def queryset(self, request, queryset):
		if self.value() == 'Pandero4':
			return queryset.filter(curso='Pandero4')
		if self.value() == 'Banderas':
			return queryset.filter(curso='Banderas')
		if self.value() == 'Tecnica Danza':
			return queryset.filter(curso='Tecnica Danza')
			
			




admin.site.register(Instructor_danza)

admin.site.register(Trainer)
@admin.register(Bailarines)
class Admin_Bailarines(admin.ModelAdmin):
	list_display=("nombre_bailarin","apellido_paterno_bailarin","apellido_materno_bailarin","edad_bailarin","curso",)
	list_filter=("nombre_bailarin",)
	list_filter=(CursoListFilter,)
	search_fields=("curso",)
	list_display_links=("apellido_paterno_bailarin",)
	list_editable=("edad_bailarin",)
# Register your models here.
