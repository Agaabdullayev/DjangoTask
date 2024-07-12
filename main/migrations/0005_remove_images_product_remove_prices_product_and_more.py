# Generated by Django 5.0.4 on 2024-07-12 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_productsid_images_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='product',
        ),
        migrations.RemoveField(
            model_name='prices',
            name='product',
        ),
        migrations.AddField(
            model_name='images',
            name='productt',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prices',
            name='productt',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.products'),
            preserve_default=False,
        ),
    ]