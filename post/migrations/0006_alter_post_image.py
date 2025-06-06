# Generated by Django 4.2.20 on 2025-05-05 06:05

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/posts/', validators=[post.models.validate_file_size]),
        ),
    ]
