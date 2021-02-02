from django.db import models
from django.db.models import fields
from .models import comment
from django import forms

class UserComment(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('comment',)

