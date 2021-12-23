from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User    
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2',]

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = models.Lead
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )


class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0)