from django.db import models

class Pupil(models.Model):
    name = models.CharField(max_length=20)
    fam = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.fam}'

