from django.db import models
from django.template.defaultfilters import slugify
class day(models.Model):
    date = models.DateField(primary_key=True)

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
        self.daySlug = (slugify(self.daySlug))
        super(day, self).save(*args, **kwargs)

    def __str__(self):
            return self.date    

