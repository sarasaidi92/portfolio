# Generated by Django 5.1.7 on 2025-03-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_academic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='date',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
