# Generated by Django 5.1.7 on 2025-03-12 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_main'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'about'},
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'activities'},
        ),
        migrations.AlterModelOptions(
            name='research',
            options={'verbose_name_plural': 'researches'},
        ),
    ]
