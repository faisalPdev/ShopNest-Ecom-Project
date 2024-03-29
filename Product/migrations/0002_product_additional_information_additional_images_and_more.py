# Generated by Django 5.0.2 on 2024-02-25 17:19

import ckeditor.fields
import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=30, prefix='prod', unique=True)),
                ('title', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(default=0, null=True)),
                ('featured_image', models.CharField(max_length=255)),
                ('discount', models.PositiveIntegerField(default=0, null=True)),
                ('brand', models.CharField(max_length=64)),
                ('available', models.PositiveIntegerField(default=0, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='123456789', length=10, max_length=30, prefix='sku', unique=True)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('top_deal_the_day', models.BooleanField(default=False)),
                ('top_featured_product', models.BooleanField(default=False)),
                ('hot_trending_product', models.BooleanField(default=False)),
                ('on_sale_product', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Additional_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('spec', models.CharField(blank=True, max_length=100, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
            options={
                'verbose_name_plural': 'Additional informations',
            },
        ),
        migrations.CreateModel(
            name='Additional_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='Short_Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
            options={
                'verbose_name_plural': 'Short Descriptions',
            },
        ),
    ]
