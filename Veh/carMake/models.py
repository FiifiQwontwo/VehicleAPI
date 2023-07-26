from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Create your models here.

class VehicleMake(models.Model):
    make_name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(blank=True, null=True, upload_to='vehicleMake/%Y/%m/%d/',
                             validators=[
                                 FileExtensionValidator(
                                     allowed_extensions=['jpeg ', 'png', 'jpg', 'webm'])])
    is_car = models.BooleanField(default=False)
    is_motor = models.BooleanField(default=False)
    is_tractor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.logo:
            # Check the image width and height here if needed
            max_size = 1 * 1024 * 1024 * 1024
            if self.logo.size > max_size:
                raise ValidationError("Image file too large ( > 1GB )")

    def __str__(self):
        return self.make_name
