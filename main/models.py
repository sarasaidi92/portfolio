from django.db import models
from ckeditor.fields import RichTextField



class Main(models.Model):
    class Meta:
        verbose_name_plural = 'main'
    web_title = models.CharField(max_length=100, blank=True)
    map = models.TextField(blank=True)

    def __str__(self):
        return f'{self.web_title}'


class Skill(models.Model):
    title = models.CharField(max_length=50, blank=True)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} ({self.percent}%)'


class About(models.Model):
    class Meta:
        verbose_name_plural = 'about'
    title = models.CharField(max_length=50, blank=True)
    text = RichTextField(blank=True)

    def __str__(self):
        return f'{self.title} ({self.text})'

class Basic(models.Model):

     avatar = models.ImageField(upload_to='photos/avatars/sa-', blank=True)
     name = models.CharField(max_length=30, blank=True)
     title = models.CharField(max_length=30, blank=True)
     email = models.EmailField(blank=True)
     phone = models.CharField(max_length=30, blank=True)
     birthday = models.DateField(blank=True)
     location = models.CharField(max_length=30, blank=True)
     linkedin = models.TextField(blank=True)
     github = models.URLField(blank=True)

     def __str__(self):
         return f'{self.title}'

class Academic(models.Model):
    title = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=50, blank=True)
    text = RichTextField(blank=True)

    def __str__(self):
        return f'{self.title}'


class Course(models.Model):
    name = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    text = RichTextField(blank=True)

    def __str__(self):
        return f'{self.name}'

class Research(models.Model):
    class Meta:
        verbose_name_plural = 'researches'
    text = RichTextField(blank=True)
    date = models.CharField(max_length=50, blank=True)

class Work(models.Model):
    text = RichTextField(blank=True)
    date = models.CharField(max_length=50, blank=True)

class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'activities'
    text = RichTextField(blank=True)
    date = models.CharField(max_length=50, blank=True)

