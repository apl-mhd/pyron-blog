from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


def validate_file_size(image_size=5):
    def validate(image):
        if image.size > image_size * 1024 * 1024:
            raise ValidationError(
                f"File size exceeds {image_size} MB, got {image.size /(1024*1024)} MB")
        return image
    return validate


def validate_image_extension(image):
    image_extension = image.name.split('.')[-1].lower()
    if image_extension not in ['jpg', 'jpeg', 'png', 'webp']:
        raise ValidationError(
            f"Unsupported file extension {image_extension}. Supported extensions are: jpg, jpeg, png, webp.")
    return image


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/posts/', null=True, blank=True, validators=[validate_file_size(), validate_image_extension])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title[0:50]}... by {self.author}"
