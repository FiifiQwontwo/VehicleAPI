from .models import VehicleModel
from rest_framework import serializers


class ModelListmakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ('model_name', 'picture')


class ModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ('make', 'model_name', 'picture')


class ModelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ('make', 'model_name', 'picture', 'created_at')


class ModelUpdateSerializer(serializers.ModelSerializer):
    picture = serializers.FileField(required=False)

    class Meta:
        model = VehicleModel
        fields = ('make', 'model_name', 'picture')

    def update(self, instance, validated_data):
        for attrs, value in validated_data.items():
            setattr(instance, att, value)
            instance.save()

            return instance


class ModelCreateSerializer(serializers.ModelSerializer):
    picture = serializers.FileField()

    class Meta:
        model = VehicleModel
        fields = ('make', 'model_name', 'picture')

    def generate_picture(self, model_name, image_extension):
        filename = f"{model_name.replace(' ', '_').lower()}.{image_extension}"

    def save(self, *args, **kwargs):
        make = self.validated_data.get('make')
        model_name = self.validated_data.get('model_name')
        picture = self.validated_data.get('picture')

        if model_name and picture:
            image_extension = piture.name.split('.')[-1]
