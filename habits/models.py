from django.db import models

# Create your models here.
class Habit(models.Model):
    name=models.CharField(max_length=100)
    streak=models.PositiveIntegerField(default=0)
    last_completed=models.DateField(null=True, blank=True)