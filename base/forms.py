from django.forms import ModelForm
from .models import Room, Message, Topic   # import the models from models.py

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  # all the fields from the model