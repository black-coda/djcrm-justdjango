from django import forms
from . import models

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