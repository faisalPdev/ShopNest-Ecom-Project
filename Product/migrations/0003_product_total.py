# Generated by Django 5.0.2 on 2024-03-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_additional_information_additional_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total',
            field=models.PositiveIntegerField(default=100, null=0),
        ),
    ]