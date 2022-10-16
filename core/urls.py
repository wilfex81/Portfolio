from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('download/', views.download_file, name= 'download'),
    #path('projects/', views.projects, name= 'projects'),
]