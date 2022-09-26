from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Suspect)
admin.site.register(Victim)
admin.site.register(Cases)
admin.site.register(UserProfile)
