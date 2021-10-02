from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('membros/', views.membros, name='membros'),
    path('membros/inseremembro/', views.insereMembro, name='inseremembro'),
    path('cargos/', views.cargos, name='cargos'),
    path('cargos/delete/<int:id>', views.deletaCargo, name='deletacargos'),
    path('cargos/inserecargos/', views.insereCargo, name='inserecargos'),
    path('departamento/', views.departamento, name='departamento'),
    path('deparamento/inseredepartamento/', views.insereDepartamento, name='inseredepartamento'),
]
 