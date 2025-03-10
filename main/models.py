from django.db import models
from ckeditor.fields import RichTextField

class Skill(models.Model):
    title = models.CharField(max_length=50, blank=True)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} ({self.percent}%)'


class About(models.Model):
    title = models.CharField(max_length=50, blank=True)
    text = RichTextField(blank=True)

    def __str__(self):
        return f'{self.title} ({self.text})'
