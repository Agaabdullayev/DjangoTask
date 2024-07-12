# Generated by Django 5.0.4 on 2024-07-12 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_productt_images_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='productImage',
            new_name='productsImage',
        ),
        migrations.RenameField(
            model_name='prices',
            old_name='productPrice',
            new_name='productsPrice',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='productDescription',
            new_name='productsDescription',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='productName',
            new_name='productsName',
        ),
        migrations.RemoveField(
            model_name='images',
            name='product',
        ),
        migrations.RemoveField(
            model_name='prices',
            name='product',
        ),
        migrations.RemoveField(
            model_name='products',
            name='categoryId',
        ),
        migrations.AddField(
            model_name='images',
            name='products',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prices',
            name='products',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='main.products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='productsCategory',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.category'),
            preserve_default=False,
        ),
    ]
