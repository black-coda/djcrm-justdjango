from django.forms import Form, ModelForm

from leads.models import Agent

class AgentModelForm(ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )