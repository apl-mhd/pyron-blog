from django.core.exceptions import ValidationError


"""We can reuse the validators for the image field in the models.py file"""


def humanreadable_file_size(bytes):
    return f"{bytes / (1024 * 1024) } MB"


def validate_file_size(image):
    if image.size > 5 * 1024 * 1024:
        raise ValidationError(
            f"File size exceeds {5} MB, got {humanreadable_file_size(image.size)}")
    return image


def validate_image_extension(image):
    image_extension = image.name.split('.')[-1].lower()
    if image_extension not in ['jpg', 'jpeg', 'png', 'webp']:
        raise ValidationError(
            f"Unsupported file extension {image_extension}. Supported extensions are: jpg, jpeg, png, webp.")
    return image
