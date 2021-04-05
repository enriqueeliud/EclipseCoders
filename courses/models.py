from django.db import models
from datetime import datetime



class Java(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'Java'


    def __str__(self):
        return self.title

    