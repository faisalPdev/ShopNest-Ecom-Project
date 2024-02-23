# Generated by Django 5.0.2 on 2024-02-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='deal',
            field=models.CharField(choices=[('Hot Deal', 'Hot Deal'), ('New Arrivals', 'New Arrivals'), ('Best Sellers', 'Best Sellers'), ('New Deal', 'New Deal')], max_length=255),
        ),
        migrations.AlterField(
            model_name='slider',
            name='deal',
            field=models.CharField(choices=[('Hot Deal', 'Hot Deal'), ('New Arrivals', 'New Arrivals'), ('Best Sellers', 'Best Sellers'), ('New Deal', 'New Deal')], max_length=255),
        ),
    ]
