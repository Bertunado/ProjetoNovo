from django.urls import path
from . import views

urlpatterns = [
   path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('pag_inicial/', views.pag_inicial, name='pag_inicial'), 

    path('fabrica-2/', views.fabrica2, name='fabrica2'),
    path('fabrica-3/', views.fabrica3, name='fabrica3'),

    path('perfiladora-fabrica2/', views.perfiladora_fabrica2, name='perfiladora_fabrica2'),
    path('cosma-perfiladoras-fabrica2/', views.cosma_perfiladoras_fabrica2, name='cosma_perfiladoras_fabrica2'),
    path('fagorGabinete-perfiladoras-fabrica2/', views.fagorGabinete_perfiladoras_fabrica2, name='fagorGabinete_perfiladoras_fabrica2'),
    path('olmaFH-perfiladoras-fabrica2/', views.olmaFH_perfiladoras_fabrica2, name='olmaFH_perfiladoras_fabrica2'),
    path('sares1-perfiladoras-fabrica2/', views.sares1_perfiladoras_fabrica2, name='sares1_perfiladoras_fabrica2'),
    path('sares2-perfiladoras-fabrica2/', views.sares2_perfiladoras_fabrica2, name='sares2_perfiladoras_fabrica2'),

    path('pintura-fabrica2/', views.pintura_fabrica2, name='pintura_fabrica2'),
    path('pintura-fabrica2-po3/', views.pintura_fabrica2_po3, name='pintura_fabrica2_po3'),
    path('pintura-fabrica2-po4/', views.pintura_fabrica2_po4, name='pintura_fabrica2_po4'),

    path('prensas-fabrica2/', views.prensas_fabrica2, name='prensas_fabrica2'),
    path('omera1_prensas-fabrica2/', views.omera1_prensas_fabrica2, name='omera1_prensas_fabrica2'),
    path('omera2_prensas-fabrica2/', views.omera2_prensas_fabrica2, name='omera2_prensas_fabrica2'),
    path('omera3_prensas-fabrica2/', views.omera3_prensas_fabrica2, name='omera3_prensas_fabrica2'),
    path('omera4_prensas-fabrica2/', views.omera4_prensas_fabrica2, name='omera4_prensas_fabrica2'),

    path('prensa-fabrica3/', views.prensa_fabrica3, name='prensa_fabrica3'),
    path('Aita-prensa-F3/', views.Aita_prensa_F3, name='Aita_prensa_F3'),
    path('fagor-prensa-F3/', views.fagor_prensa_F3, name='fagor_prensa_F3'),

    path('perfiladora-fabrica3/', views.perfiladora_fabrica3, name='perfiladora_fabrica3'),
    path('jundiai-perfiladorasF3/', views.jundiai_perfiladorasF3, name='jundiai_perfiladorasF3'),
    path('sares3-perfiladorasF3/', views.sares3_perfiladorasF3, name='sares3_perfiladorasF3'),
    path('sares4-perfiladorasF3/', views.sares4_perfiladorasF3, name='sares4_perfiladorasF3'),

    path('pintura-fabrica3/', views.pintura_fabrica3, name='pintura_fabrica3'),
    path('pinturaliquidaF3/', views.pinturaliquidaF3, name='pinturaliquidaF3'),

    



    ]
