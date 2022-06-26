from django.forms import ModelForm
from .models import Patient, Clinicaldata

class PatientForm(ModelForm):
    model = Patient
    class Meta:
        fields = '__all__'

class ClinicaldataForm(ModelForm):
    class Meta:
        model = Clinicaldata
        fields = '__all__'
    
