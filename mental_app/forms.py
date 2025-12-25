# mental_app/forms.py
from django import forms

class PredictionForm(forms.Form):
    country = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')])
    exercise_level = forms.ChoiceField(choices=[('Low','Low'),('Medium','Medium'),('High','High')])
    diet_type = forms.ChoiceField(choices=[('Poor','Poor'),('Average','Average'),('Good','Good')])
    sleep_hours = forms.FloatField()
    stress_level = forms.ChoiceField(choices=[('Low','Low'),('Medium','Medium'),('High','High')])
    work_hours_per_week = forms.IntegerField()
    screen_time_per_day = forms.FloatField()
    social_interaction_score = forms.FloatField()
    happiness_score = forms.FloatField()