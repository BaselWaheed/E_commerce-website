# Generated by Django 3.1.5 on 2022-08-26 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='total_price',
            new_name='pro_total_price',
        ),
        migrations.AddField(
            model_name='product',
            name='pro_description',
            field=models.TextField(default=1, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pro_status',
            field=models.CharField(choices=[('av', 'available'), ('un', 'unavailable')], default=1, max_length=50, verbose_name='status'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='FavouriteProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='pro_favourite',
            field=models.ManyToManyField(through='product.FavouriteProduct', to=settings.AUTH_USER_MODEL, verbose_name='favourite'),
        ),
    ]
