
from django.conf.urls import url

urlpatterns = [
   url('foods/', views.FoodAPIView.as_view()),
]
