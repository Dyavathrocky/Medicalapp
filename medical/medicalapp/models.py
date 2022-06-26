from django.db import models

# Create your models here.

class Patient(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname+"   "+ self.lastname

    
class Clinicaldata(models.Model):
    component_choices = [('hw', 'height/weight'),('bp','bloodpresure'),('hr','heartrate')]
    componentname = models.CharField(max_length=30, choices=component_choices)
    componentvalue = models.CharField(max_length=30)
    mesureddate = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient


