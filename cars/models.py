from django.db import models

# Create your models here.
class Karysel(models.Model):
    image = models.ImageField(upload_to='')


class Catal(models.Model):
    image = models.ImageField(upload_to='')
    description = models.TextField()


