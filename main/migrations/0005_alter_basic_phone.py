# Generated by Django 5.1.7 on 2025-03-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_basic_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
