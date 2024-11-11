from django.contrib import admin
from .models import Movieinfo, Director, Censorinfo, Actor

# Register your models here.
admin.site.register(Movieinfo)
admin.site.register(Director)
admin.site.register(Censorinfo)
admin.site.register(Actor)
