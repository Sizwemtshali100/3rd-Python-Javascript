from django.db import models

# Create your models here.
class TestModel(models.Model):
    Name = models.CharField(max_length=30, blank=True)
    Surname = models.CharField(max_length=30, blank=True)
    Weight = models.CharField(max_length=30, blank=True)
    Height = models.CharField(max_length=30, blank=True)
    Gender = models.CharField(max_length=6, blank=True, null=True)
    Outcome = models.CharField(max_length=30, blank=True)
    Activity = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.Name
