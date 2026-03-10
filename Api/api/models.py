

from django.db import models

# Create your models here.


class programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname
# este es un comentario de una sola línea
# otro comentario de una sola línea
