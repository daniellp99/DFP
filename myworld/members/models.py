from ast import ClassDef
from django.db import models

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lasttname = models.CharField(max_length=255)