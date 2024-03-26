from django.db import models
import uuid

class Activity(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    size = models.FloatField()
    name = models.CharField(max_length=100)
    valueActivity = models.FloatField()
    totalActivity = models.FloatField()