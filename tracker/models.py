from django.db import models
from django.template.defaultfilters import slugify


class day(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateField()

    #symptoms
    fatigue = models.IntegerField(default=0)
    nausea = models.IntegerField(default=0)
    bloated = models.IntegerField(default=0)

    #foods
    dairy = models.IntegerField(default=0)
    gluten = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)

    daySlug = models.SlugField(unique=True, default='day-')

    def save(self, *args, **kwargs):
        self.daySlug = (slugify(self.id))
        super(day, self).save(*args, **kwargs)

    def __str__(self):
            return str(self.date)    

