# Generated by Django 2.2.14 on 2020-08-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_remove_photos_compressed_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='compressed_photo',
            field=models.ImageField(default='compressed_images/default.jpg', upload_to='compressed_images/'),
        ),
    ]
