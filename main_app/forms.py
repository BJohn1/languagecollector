from django.forms import ModelForm
from .models import Upskill

class UpskillForm(ModelForm):
  class Meta:
    model = Upskill
    fields = ['date', 'practice']