from django.db import models

#Service models
class Service(models.Model):
    introduction = models.TextField()
    service_name = models.CharField(max_length=120)
    details = models.TextField()

    def __str__(self):
        return self.service_name

#Projects models
class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    github_name = models.CharField(blank= True, max_length=120 )
    liver_server_name = models.CharField(blank= True, max_length= 120)
    live_server = models.URLField(blank=True, max_length=120)
    github = models.URLField(blank=True, max_length=120)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

#About models
class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    resume = models.FileField(max_length=254, upload_to='documents/')
    image = models.ImageField(upload_to='images/')
    resume_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

#contact models
class Contact(models.Model):
    phone = models.CharField(null=False, blank=False, unique=True, max_length = 128)
    address = models.CharField(("address"), max_length=128)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.address

#footer models
class Footer(models.Model):
    title = models.CharField(max_length=150)
    linkedIn = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    twiter = models.URLField(blank=True)

    def __str__(self):
        return self.title
        