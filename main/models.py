from django.db import models

class ModelInfo(models.Model):
    name = models.CharField()
    slug = models.SlugField()
    description = models.CharField()
    img = models.ImageField(upload_to = 'sectors/')

    class Meta:
        verbose_name = 'Інформація_про_сектор'
        verbose_name_plural = 'Інформація_про_сектори'
