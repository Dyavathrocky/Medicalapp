from pyexpat import model
from django.contrib import admin
from .models import Patient, Clinicaldata
from django.contrib.admin import ModelAdmin

# Register your models here.

class extend(ModelAdmin):
    search_fields = ['firstname']
    class META:
        fields = '__all__'

admin.site.register(Patient , extend)
admin.site.register(Clinicaldata)
