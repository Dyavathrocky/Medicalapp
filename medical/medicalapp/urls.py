from django.contrib import admin
from django.urls import path , include
from .views import test , PatientListView , PatientCreateView , PatientUpdateView , PatientDeleteView, adddata ,analyze

urlpatterns = [
    path('list/', PatientListView.as_view(), name='list'),
    path('create/', PatientCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PatientUpdateView.as_view(), name='update' ),
    path('delete/<int:pk>/', PatientDeleteView.as_view(), name='delete'),
    path('adddata/<int:pk>/',adddata , name="adddata"),
    path('analyze/<int:pk>/', analyze, name='analyse'),
]
