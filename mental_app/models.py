from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    country = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    exercise_level = models.CharField(max_length=50)
    diet_type = models.CharField(max_length=50)
    sleep_hours = models.FloatField()
    stress_level = models.CharField(max_length=50)
    mental_health_condition = models.CharField(max_length=100, blank=True, null=True)
    work_hours_per_week = models.IntegerField()
    screen_time_per_day = models.FloatField()
    social_interaction_score = models.FloatField()
    happiness_score = models.FloatField()

    def __str__(self):
        return f"{self.country} - {self.age} - {self.gender}"
