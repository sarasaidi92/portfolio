from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=50, blank=True)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} {self.percent}%'
