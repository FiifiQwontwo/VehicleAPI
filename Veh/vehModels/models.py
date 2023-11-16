from django.db import models
from carMake.models import VehicleMake
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Create your models here.
class VehicleModel(models.Model):
    make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE, related_name="models")
    model_name = models.CharField(max_length=255)
    picture = models.ImageField(blank=True, null=True, upload_to='vehicleMake/%Y/%m/%d/',
                             validators=[
                                 FileExtensionValidator(
                                     allowed_extensions=['jpeg ', 'png', 'jpg', 'webm'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.picture:
            # Check the image width and height here if needed
            max_size = 1 * 1024 * 1024 * 1024
            if self.picture.size > max_size:
                raise ValidationError("Image file too large ( > 1GB )")

    def __str__(self):
        return self.model_name

