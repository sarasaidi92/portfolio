from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    date = models.DateTimeField( blank=True)

    def __str__(self):
        return self.name




