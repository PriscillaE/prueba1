from django import template
from ..models import Bailarines

register = template.Library()


@register.inclusion_tag('tags.html')
def firstTAG():
	M1=Bailarines.manager.all().order_by('curso')
	return {'var1':M1}