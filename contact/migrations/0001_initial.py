# Generated by Django 5.1.7 on 2025-03-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('message', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
