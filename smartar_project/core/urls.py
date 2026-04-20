from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]