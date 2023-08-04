from .models import BodyType
from rest_framework import serializers


class ListBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ('id', 'body_type', 'picture', 'description')


class CreateBodyType(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ('id', 'body_type', 'picture', 'description')

    def save(self, *args, **kwargs):
        body_type = self.validated_data.get('body_type')
        picture = self.validated_data.get('picture')
        description = self.validated_data.get('description')

        if body_type and picture:
            new_body = BodyType(
                body_type=body_type,
                picture=picture,
                description=description,
            )
            new_body.save()
            return new_body


class UpdateBodyTypeSerializer(serializers.ModelSerializer):
    picture = serializers.FileField(required=False)

    class Meta:
        model = BodyType
        fields = '__all__'

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
