from rest_framework import serializers
from recongnition import models


class PlantaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlantaModel
        fields = [
            'id',
            'nombre',
            'nombreCientifico',
            'descripcion',
            'cuidados'
        ]

        def create(self, data):
        
            newPlanta = models.PlantaModel.objects.create(
                nombre = data.get("nombre"),
                nombreCientifico  = data.get("nombreCientifico"),
                descripcion = data.get("descripcion"),
                cuidados = data.get("cuidados") 
            )

            return newPlanta