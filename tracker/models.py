from django.db import models


class Day(models.Model):
    date = models.CharField(max_length=10, unique=True)

    #symptoms
    fatigue = models.IntegerField(default=0)
    nausea = models.IntegerField(default=0)
    bloated = models.IntegerField(default=0)

    #foods
    dairy = models.IntegerField(default=0)
    gluten = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)

    def __str__(self):
            return str(self.date)
