# Generated by Django 3.0.3 on 2020-09-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0010_album_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]