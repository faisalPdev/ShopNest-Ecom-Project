# Generated by Django 5.0.2 on 2024-06-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_alter_account_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
