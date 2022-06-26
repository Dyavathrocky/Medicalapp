from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView ,UpdateView , CreateView , DeleteView
from django.urls import reverse_lazy

from .models import Patient,Clinicaldata
from .forms import PatientForm, ClinicaldataForm


# Create your views here.

def test(request):
    return HttpResponse("hi this is rakesh")


class PatientListView(ListView):
    model = Patient
    template_name = 'medicalapp/listview.html'
    context_object_name = 'list_view'
    

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'medicalapp/create.html'
    context_object_name = 'create_view'
    fields = '__all__'
    success_url = reverse_lazy('list')

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'medicalapp/update.html'
    context_object_name = 'udate_view'
    fields = '__all__'
    success_url = reverse_lazy('list')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('list')


def adddata(request, **kwargs):
    form = ClinicaldataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicaldataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    return render(request, 'medicalapp/adddata.html', {'form':form , 'patient':patient})


def analyze(request, **kwargs):
    data = Clinicaldata.objects.filter(id=kwargs['pk'])
    responsedata = []
    for eachentry in data:
        if eachentry.componentname == 'hw':
            heightandwidth = eachentry.componentvalue.split('/')
            feettometers = float(heightandwidth[0])*0.4536
            BMI = (float(heightandwidth[1]))/(feettometers*feettometers)
            bmientry = Clinicaldata()
            bmientry.componentname = 'BMI'
            bmientry.componentvalue = BMI
            responsedata.append(bmientry)
        responsedata.append(eachentry)
    return render(request, 'medicalapp/genarate.html', {'data':responsedata , 'patient':data})
