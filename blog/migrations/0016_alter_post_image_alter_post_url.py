# Generated by Django 4.0 on 2022-01-09 15:38

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=blog.models.user_directory),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]