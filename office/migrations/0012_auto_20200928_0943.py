# Generated by Django 3.0.3 on 2020-09-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0011_auto_20200928_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, default=None, upload_to='gallery'),
        ),
    ]