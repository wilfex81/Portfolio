from django.shortcuts import render

from core.models import About, Contact, Footer, Project, Service


#HomePage
def home(request):
    return render(request, 'index.html')

#Services
def services(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'index.html', context)

#Projects
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'index.html', context)

#About
def about(request):
    about = About.objects.all()
    context = {'about': about}
    return render(request, 'index.html', context)

#Contact
def about(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'index.html', context)

#Footer
def Footer(request):
    footer = Footer.objects.all()
    context = {'footer': footer}
    return render(request, 'index.html', context)

