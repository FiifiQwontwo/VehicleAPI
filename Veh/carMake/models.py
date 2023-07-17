from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Create your models here.

class VehicleMake(models.Model):
    make_name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, upload_to='vehicleMake/%Y/%m/%d/',
                             validators=[
                                 FileExtensionValidator(
                                     allowed_extensions=['jpeg ', 'png', 'jpg', 'webm'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.logo:
            # Check the image width and height here if needed
            max_size = 1 * 1024 * 1024 * 1024
            if self.logo.size > max_size:
                raise ValidationError("Image file too large ( > 50MB )")