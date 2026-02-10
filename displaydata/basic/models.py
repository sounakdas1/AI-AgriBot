from django.db import models

class MyData(models.Model):
    temp = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
