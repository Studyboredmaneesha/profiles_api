from django.shortcuts import render
from rest_framework import generics, filters
from search1.models import Food
from search1.serializers import FoodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class FoodAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, )
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
