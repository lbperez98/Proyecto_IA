
from distutils.log import debug
from recongnition import models,serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from mysite.settings import DEBUG


# Create your views here.
class PlantaView(ModelViewSet):

    queryset = models.PlantaModel.objects.all()
    serializer_class = serializers.PlantaSerializer
    
    @action(methods = ['get'], detail= False)
    def get_Planta(self, request):
        
        nombrePlanta = request.GET.get('nombrePlanta')
        planta = models.PlantaModel.objects.filter(
            nombre = nombrePlanta
        )

        datos = self.get_serializer(planta, many = True)

        return Response(datos.data)

