from rest_framework import serializers
from .models import Fuel


class ListFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('id', 'fuel_type')


class CreateFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('fuel_type',)

    def save(self, *args, **kwargs):
        fuel_type = self.validated_data.get('fuel_type')

        new_fuel_type = Fuel(
            fuel_type=fuel_type,
        )
        new_fuel_type.save()
        return new_fuel_type


class UpdateFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('fuel_type',)

    def update(self, instance, validated_data):
        for attrs, value in validated_data.items():
            setattr(instance, attrs, value)
        instance.save()

        return instance
