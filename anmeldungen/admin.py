from django.contrib import admin
from .models import Nutzer, Events, KW

# Register your models here.
admin.site.register(Nutzer)
admin.site.register(Events)
admin.site.register(KW)
