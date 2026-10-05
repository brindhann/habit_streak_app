from django.db import models
from datetime import date, timedelta

# Create your models here.
class Habit(models.Model):
    name=models.CharField(max_length=100)
    streak=models.PositiveIntegerField(default=0)
    last_completed=models.DateField(null=True, blank=True)

    def complete(self):
        today=date.today()

        if self.last_completed==today:
            return

        if self.last_completed==today-timedelta(days=1):
            self.streak+=1
        else:
            self.streak=1

        self.last_completed=today
        self.save()

    def undo_completion(self):
        today=date.today()

        if self.last_completed!=today:
            return

        if self.streak<=1:
            self.streak=0
            self.last_completed=None
        else:
            self.streak-=1
            self.last_completed=today-timedelta(days=1)

        self.save()

    def __str__(self):
        return self.name