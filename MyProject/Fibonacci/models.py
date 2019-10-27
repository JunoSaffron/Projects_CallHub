from django.db import models
from django.forms import ModelForm
# Create your models here.

class Input(models.Model):
    r = models.IntegerField()
    class Meta:
        abstract = True
        app_label = 'Fibonacci'

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'