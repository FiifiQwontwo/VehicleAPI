from .models import VehicleModel
from rest_framework import serializers


class ModelListSerializer(serializers.ModelSerializer):
    make = serializers.StringRelatedField()


    class Meta:
        model = VehicleModel
        fields = ("make", "model_name","picture")

    def get_make(self, obj):
        return obj.make.make_name if obj.make else None


class CreateModel(serializers.ModelSerializer):
    picture = serializers.FileField()
    class Meta:
        model = VehicleModel
        fields = ('id', 'make', 'model_name', 'picture')

    def generate_filename(self, make_name, image_extension):

        filename = f"{model_name.replace(' ', '_').lower()}.{image_extension}"
        return filename

    def save(self, *args, **kwargs):
        make = self.validated_data.get('make')
        picture = self.validated_data.get('picture')
        model_name = self.validated_data.get('model_name')

        if model_name and picture:
            image_extension = picture.name.split('.')[-1]
            filename = self.generate_filename(model_name, image_extension)
            picture.name = filename


            new_model = VehicleModel(
                make=make,
                model_name=model_name,
                picture=picture,
            )
            new_model.save()
            return new_model
