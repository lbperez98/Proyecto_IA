from django.shortcuts import render
from recongnition import models,serializers
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class PlantaView(ModelViewSet):

    queryset = models.PlantaModel.objects.all()
    serializer_class = serializers.PlantaSerializer
    

