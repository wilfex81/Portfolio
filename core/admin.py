from django.contrib import admin

from core.models import About, Contact, Footer, Project, Service

# Register your models here.

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Footer)
