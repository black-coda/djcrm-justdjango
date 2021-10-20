from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from leads.models import Agent
from . forms import AgentModelForm
# Create your views here.

class AgentListView(LoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'
    def get_queryset(self):
        return Agent.objects.all()
    """
    model = Agent
    queryset = Agent.objects.all()
    """

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self, form):
        print(self)
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)