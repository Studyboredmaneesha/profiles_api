from django.shortcuts import render
from rest_framework import generics, filters
from search1.models import Food
from search1.serializers import FoodSerializer



# Create your views here.
class FoodAPIView(generics.ListCreateAPIView):
    search_fields = ['name', 'price']
    filter_backends = (filters.SearchFilter, )
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
