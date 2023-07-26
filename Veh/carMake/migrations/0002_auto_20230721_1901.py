# Generated by Django 3.2 on 2023-07-21 19:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carMake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemake',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='vehicleMake/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg ', 'png', 'jpg', 'webm'])]),
        ),
        migrations.AlterField(
            model_name='vehiclemake',
            name='make_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]