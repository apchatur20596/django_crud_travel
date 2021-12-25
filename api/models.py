from django.db import models

# Create your models here.

class TravelPlans(models.Model):
    title = models.CharField(max_length=100)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title