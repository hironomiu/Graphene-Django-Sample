from django.db import models
from django.db.models.fields.related import ForeignKey


class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
