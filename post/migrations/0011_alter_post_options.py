# Generated by Django 4.2.20 on 2025-05-06 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
    ]
