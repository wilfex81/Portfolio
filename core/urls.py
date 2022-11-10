from django.urls import path
from . import views
from django.views.static import serve
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'home'),
    #path('download_cv/', views.download_cv, name= 'download_cv'),
    #path('projects/', views.projects, name= 'projects'),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)