# Generated by Django 5.1.7 on 2025-03-13 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(default='python', max_length=50, null=True),
        ),
    ]
