from django.shortcuts import render

from core.models import About, Contact, Footer, Project, Service


#HomePage
def home(request):
    services = Service.objects.all()
    #projects = Project.objects.all()
    abouts = About.objects.all()
    contacts = Contact.objects.all()
    footer = Footer.objects.all()
    context = {'projects': projects, 'services': services, 
            'abouts': abouts,'contacts': contacts, 'footer': footer}
    return render(request, 'index.html', context)

def projects(request):
        projects = Project.objects.all()
        context = {'projects': projects}
        return render(request, 'index.html', context)