# Generated by Django 4.0 on 2022-01-09 14:05

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to=blog.models.user_directory),
        ),
    ]
