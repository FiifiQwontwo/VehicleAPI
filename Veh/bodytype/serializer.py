from .models import BodyType
from rest_framework import serializers


class ListBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ('id', 'body_type', 'picture', 'description')


class CreateBodyType(serializers.ModelSerializer):
    picture = serializers.FileField(required=True)

    class Meta:
        model = BodyType
        fields = ('id', 'body_type', 'picture', 'description')

    def generatefilename(self, body_type, image_extension):
        filename = f"{body_type.replace('', '_').lower()}.{image_extension}"
        return filename

    def save(self, *args, **kwargs):
        body_type = self.validated_data.get('body_type')
        picture = self.validated_data.get('picture')
        description = self.validated_data.get('description')

        if body_type and picture:
            image_extension = picture.name.split('.')[-1]
            filename = self.generatefilename(body_type, image_extension)
            picture.name = filename

            new_body =BodyType(
                body_type=body_type,
                picture=picture,
                description=description,
            )
            new_body.save()
            return new_body

