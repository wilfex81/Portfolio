import mimetypes
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


from core.models import About, Contact, Footer, Project, Service


#HomePage
csrf_exempt 
def home(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    abouts = About.objects.all()
    contacts = Contact.objects.all()
    footer = Footer.objects.all()
    context = {'projects': projects, 'services': services, 
            'abouts': abouts,'contacts': contacts, 'footer': footer}
    return render(request, 'index.html', context)
    
csrf_exempt
def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/resume")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404