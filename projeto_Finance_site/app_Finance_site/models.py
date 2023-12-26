from django.db import models

# Create your models here.


class Create_database(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    value = models.FloatField()