from django.contrib import admin
from django.contrib.admindocs import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('medicos/', views.medicos, name='medicos'),
    path('tratamientos/', views.tratamientos, name='tratamientos'),
]