# Generated by Django 5.1.7 on 2025-03-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_title', models.CharField(blank=True, max_length=100)),
                ('map', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'main',
            },
        ),
    ]
