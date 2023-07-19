from rest_framework import serializers
from .models import VehicleMake


class ListVehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleMake
        fields = ('make_name', 'logo')


class CreateVehicleSerializers(serializers.ModelSerializer):
    logo = serializers.FileField()

    class Meta:
        model = VehicleMake
        fields = ('make_name', 'logo')

    def generate_filename(self, make_name, image_extension):
        # Generate a unique filename based on the model name
        filename = f"{make_name.replace(' ', '_').lower()}.{image_extension}"
        return filename

    def save(self, **kwargs):
        make_name = self.validated_data.get('make_name')
        logo = self.validated_data.get('logo')

        if make_name and logo:
            image_extension = logo.name.split('.')[-1]
            filename = self.generate_filename(make_name, image_extension)
            logo.name = filename

            new_vehicle = VehicleMake(
                make_name=make_name,
                logo=logo,
            )
            new_vehicle.save()
            return new_vehicle
