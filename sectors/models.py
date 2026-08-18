from django.db import models

class Sectors(models.Model):
    title = models.CharField()
    description = models.TextField()
    wave = models.IntegerField()
    image = models.CharField()

    def __str__(self):
      return self.title 
