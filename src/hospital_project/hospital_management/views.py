from django.shortcuts import render
from rest_framework import generics, filters
from hospital_management.models import Patient
from hospital_management.serializers import PatientSerializer



# Create your views here.
class PatientAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, )
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Create your views here.
