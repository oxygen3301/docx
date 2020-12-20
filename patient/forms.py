from django.forms import ModelForm
from .models import Log

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ['temperature', 'pulse', 'bp', 'respiratory_rate', 'oxygen_saturation', 'doctor_comment', 'user']