from rest_framework import serializers
from .models import Vacuna, AplicacionVacuna

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['id', 'nombre', 'descripcion']

class AplicacionVacunaSerializer(serializers.ModelSerializer):
    vacuna = VacunaSerializer()  # Para incluir la información de la vacuna

    class Meta:
        model = AplicacionVacuna
        fields = ['id', 'mascota', 'vacuna', 'fecha_aplicacion', 'proximo_refuerzo']
        read_only_fields = ['mascota']

    def create(self, validated_data):
        vacuna_data = validated_data.pop('vacuna')
        # Buscar o crear la vacuna (dependiendo de la lógica que necesites)
        vacuna_obj, created = Vacuna.objects.get_or_create(**vacuna_data)
        aplicacion = AplicacionVacuna.objects.create(vacuna=vacuna_obj, **validated_data)
        return aplicacion

    def update(self, instance, validated_data):
        # Permite actualizar la aplicación sin cambiar la vacuna asociada
        instance.fecha_aplicacion = validated_data.get('fecha_aplicacion', instance.fecha_aplicacion)
        instance.proximo_refuerzo = validated_data.get('proximo_refuerzo', instance.proximo_refuerzo)
        instance.save()
        return instance