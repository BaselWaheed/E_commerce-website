# Generated by Django 3.1.5 on 2022-08-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20220827_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='im_photo',
            field=models.ImageField(blank=True, null=True, upload_to='image', verbose_name='image'),
        ),
    ]