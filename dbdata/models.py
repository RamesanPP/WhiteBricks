from django.db import models

# Create your models here.

class PG(models.Model):
    name = models.CharField(max_length=30)
    headcount = models.IntegerField(default=1)
    pgtype = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    img = models.ImageField(upload_to='pics',default='property-img-default.gif')
    rent = models.IntegerField()
    deposit = models.IntegerField()
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    