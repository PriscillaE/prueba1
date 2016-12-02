"""p1ec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from home.views import About_view
from bases.views import bailarines_list
from bases.views import instructores_list
from bases.views import bailarines_register
from bases.views  import Bailarines_register_view
from bases. views import Index_view
from bases.views import instructores_register
from bases.views import Instructores_register_view
from bases.views import Register_Bailarines
from bases.views import Register_Instructores
from django.contrib.auth.views import login, logout_then_login
from bases.views import Sigup
from bases.views import consulta,consulta2,consulta3,consulta4,auxiliar,imagenes,Bailarines_Detail,buscar_bailarines,bailarines_report,Update_bailarines, Bailarines_update, Detail_Trainer
from django.conf.urls import url,include 
from django.conf import settings
from django.conf.urls.static import static
from wsjanson.views import wsBailarines, xmBailarines, wsInstructor_danza

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('social.apps.django_app.urls',namespace ='social')),
    url(r'^$', login, {'template_name': 'index.html'}, name = 'login'),
    url(r'^salir/$', logout_then_login, name ='logout'),
    url(r'^about/$', About_view.as_view(), name = 'About_view'),
    url(r'^list_bailarines/$', bailarines_list, name = 'bailarines_list'),
    url(r'^list_instructores/$', instructores_list, name = 'instructores_list'),
    url(r'^register_bailarines/$', bailarines_register, name = 'Bailarines_register_view'),
    url(r'^$', Index_view.as_view(), name = 'Index_view'),
    url(r'^instructores_register/$', instructores_register, name = 'Instructores_register_view'),
    url(r'register_bailarines2/$',Register_Bailarines.as_view(), name = 'bailarines_register2'),
    url(r'instructores_register2/$',Register_Instructores.as_view(), name ='instructores_register2'),
    url(r'sigup/$',Sigup.as_view(), name = 'Sigup_view'),
    url(r'^consultas/$', consulta, name= 'consultas'),
    url(r'^consultas2/$', consulta2, name= 'consultas2'),
    url(r'^consultas3/$', consulta3, name= 'consultas3'),
    url(r'^consultas4/$', consulta4, name= 'consultas4'),
    url(r'^ConsultasG/$', auxiliar.as_view(), name= 'auxiliar'),
    url(r'^Galeria/$',imagenes.as_view(), name = 'imagenes'),
    url(r'^detail_bailarines/(?P<pk>\d+)$',Bailarines_Detail.as_view(),name= 'Bailarines_Detail_view'),
    url(r'^Reporte/$',bailarines_report.as_view(), name = 'bailarines_report_view'),
    url(r'^ingresar/$', buscar_bailarines, name= 'tomar_dato_view'),
    url(r'^updates/(?P<pk>\d+)$', Update_bailarines.as_view(), name = 'update_bailarines_view'),
    url(r'^actualizar/(?P<pk>\d+)$', Bailarines_update, name = 'bailarines_actualizar_view'),
    url(r'^bailarines/', wsBailarines, name = 'Bailarines_json'),
    url(r'^bailarines1/', xmBailarines, name = 'Bailarines_xml'),
    url(r'^instructores/', wsInstructor_danza, name = 'Instructores_json'),
    url(r'^detail_trainer/(?P<pk>\d+)$',Detail_Trainer.as_view(),name= 'Detail_Trainer_view'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
   
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)