from django.db import models

# Create your models here.

class Nutzer(models.Model):
    mail = models.EmailField(max_length=254)
    name = models.CharField(max_length=600)
    datum = models.DateField(auto_now=False, auto_now_add=True)
    events = models.ManyToManyField('Events')
    def __str__(self):
        return str(self.mail + " am " + str(self.datum))
    
class Events(models.Model):
    kw = models.ForeignKey('KW')
    titel = models.CharField(max_length=200)
    beschreibung = models.CharField(max_length=600)
    termin = models.DateTimeField(auto_now=False, auto_now_add=False)
    ort = models.CharField(max_length=140)
    strasse = models.CharField(max_length=140)
    plz = models.IntegerField(max_length=None)
    ort = models.CharField(max_length=100)
    def __str__(self):
        return self.titel
        
class KW(models.Model):
    kw = models.IntegerField()
    jahr = models.IntegerField()
    active = models.BooleanField(default=False)
    def __str__(self):
        return str(self.jahr)+"-"+str(self.kw)