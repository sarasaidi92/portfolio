# Generated by Django 5.1.7 on 2025-03-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.PositiveIntegerField(blank=True, default=0)),
                ('birthday', models.DateField(blank=True)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('linkedin', models.TextField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('instagram', models.TextField(blank=True)),
                ('whatsapp', models.TextField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
