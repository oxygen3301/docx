from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Log(models.Model):
    temperature = models.FloatField()
    pulse = models.IntegerField(null=True)
    bp = models.CharField(max_length = 7)
    respiratory_rate = models.FloatField()
    oxygen_saturation = models.FloatField()
    doctor_comment = models.TextField(blank = True)
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)