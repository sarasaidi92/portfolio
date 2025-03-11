# Generated by Django 5.1.7 on 2025-03-11 07:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(blank=True)),
                ('date', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
