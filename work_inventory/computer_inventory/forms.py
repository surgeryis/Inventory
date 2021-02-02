from django import forms
from .models import *

class ComputersForms(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('operating_system','computer_name', 'serial_number', 'operating_system','user_name',
                  'person_full_name','comments', 'model_number', 'location' )