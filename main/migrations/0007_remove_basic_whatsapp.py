# Generated by Django 5.1.7 on 2025-03-10 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_basic_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic',
            name='whatsapp',
        ),
    ]
