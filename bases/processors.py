def  bailarines_proces(request):
# Create fixed data structures to pass to template
# data could equally come from database queries
# web services or social APIs
	bailarines_items = 'Los bailarines de la academia'
	return {'BAILARINES_ITEMS': bailarines_items}