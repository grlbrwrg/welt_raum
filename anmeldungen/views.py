from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django import forms
from .models import Nutzer, Events, KW
from django.core.mail import send_mail
from .forms import EventAuswahlForm
from django.contrib.auth.decorators import login_required



# Create your views here.


from datetime import date, timedelta

# Funktion um das Datum vom Start und Ende einer Kalenderwoche anzuzeigen
def get_week_days(year, week):
    d = date(year,1,1)
    if(d.weekday()>3):
        d = d+timedelta(7-d.weekday())
    else:
        d = d - timedelta(d.weekday())
    dlt = timedelta(days = (week-1)*7)
    start = d + dlt
    end = d + dlt + timedelta(days=6)
    return str(start.day) + "." + str(start.month) + " bis " + str(end.day) + "." + str(end.month)

# Erstellt das Formular für die Anmeldung
class anmeldungForm(ModelForm):
    class Meta:
        model = Nutzer
        fields = ['mail', 'name', 'events']
        widgets = {'events': forms.CheckboxSelectMultiple}

# Anmeldung für Events        
def anmeldung(request):
    # zieht alle Events für KWs, deren Status ""active" auf True gesetzt wurde
    kw = KW.objects.filter(active=True)
    datum = ""
    # wenn mehr als eine aktive KW gibt, werden die Datumsinformationen mit Komma hintereinander geschrieben
    if len(kw) >= 2:
        for i in kw:
            p = get_week_days(i.jahr,i.kw)
            datum = datum + str(p) + ", "
        datum = datum[:-2]
    else:
        for i in kw:
            p = get_week_days(i.jahr,i.kw)
            datum = str(p)
    # zieht alle Events, die aktiven KWs zugeordnet sind
    events = Events.objects.filter(kw=kw).filter(deactive=False)
    # werden Events über das Formular gesendet, werden sie in die Datenbank gespeichert & eine Bestätigungsmail wird geschickt. Weiterleitung auf die Dank-Seite
    if request.method == 'POST':
        inhalt = anmeldungForm(request.POST)
        if inhalt.is_valid():
            inhalt.save()
            return HttpResponseRedirect('/erfolg/?=')

        else:
            return HttpResponse("FEHLER! Bitte wende dich an welt_raum@posteo.de")
        
        
    # wenn (aus dem Newsletter) GET-Informationen mitgeschickt wurden (mail, fname & lname), werden sie schon ins Formular eingefügt
    if request.GET:
        user = request.GET
        mail = user.get('mail')
        name = str(user.get('fname')) + " " + str(user.get('lname'))
        anmeldung = anmeldungForm(initial={'mail':mail,'name':name,})
        anmeldung.fields['events'].queryset = events
        return render(request, 'anmeldungen/index.html',{'anmeldung':anmeldung,'events':events,'datum':datum})
    # wenn die Seite ohne weitere Informationen aufgerufen wird, wird ein leeres Formular erstellt
    anmeldung = anmeldungForm()    
    anmeldung.fields['events'].queryset = events
    return render(request, 'anmeldungen/index.html',{'anmeldung':anmeldung,'events':events,'datum':datum})
    
def erfolg(request):
    if request.GET:
        return render(request, 'anmeldungen/erfolg.html',{})
    else:
        return HttpResponseRedirect('/anmeldung/')


@login_required()        
def teilnehmer(request):
    nutzer = {}
    if request.method == 'POST':
        inhalt = EventAuswahlForm(request.POST)
        if inhalt.is_valid():
            nutzer = Nutzer.objects.filter(events = inhalt.cleaned_data['event'])

    eventauswahl = EventAuswahlForm()
    return render(request, 'anmeldungen/teilnehmer.html',{'eventauswahl':eventauswahl,'nutzer':nutzer})
        

        
    