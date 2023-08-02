from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Create your models here.
class BodyType(models.Model):
    body_type = models.CharField(max_length=25, unique=True)
    picture = models.ImageField(blank=True, null=True, upload_to='bodyType/%Y/%m/%d/',
                                validators=[
                                    FileExtensionValidator(
                                        allowed_extensions=['jpeg ', 'png', 'jpg', 'webm'])])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body_type

    def clean(self):
        if self.picture:
            # Check the image width and height here if needed
            max_size = 1 * 1024 * 1024 * 1024
            if self.picture.size > max_size:
                raise ValidationError("Image file too large ( > 1GB )")
