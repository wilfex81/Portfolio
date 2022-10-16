import mimetypes
import os
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
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
def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'cv.pdf'
    # Define the full file path
    filepath = BASE_DIR + '/filedownload/Files/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

# def projects(request):
#         projects = Project.objects.all()
#         context = {'projects': projects}
#         return render(request, 'index.html', context)