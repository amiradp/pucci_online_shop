# Generated by Django 5.0.6 on 2024-06-07 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.size'),
            preserve_default=False,
        ),
    ]