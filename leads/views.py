from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from . models import Agent, Lead
from . import forms
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.SignUpForm
    
    def get_success_url(self):
        return reverse('login')


class LandingView(generic.TemplateView):
    template_name = "landing.html"

def landing_page_view( request,*args, **kwargs):
    return render(request,'landing.html' ,*args, **kwargs,)
########################################

class LeadListView(LoginRequiredMixin,generic.ListView):
    template_name       = 'leads/lead_list.html'
    context_object_name = 'leads'
    queryset            = Lead.objects.all()


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads':leads
    }
    return render(request, 'leads/lead_list.html', context)

#######################################

class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name       = 'leads/lead_detail.html'
    context_object_name = 'lead'
    queryset            = Lead.objects.all()


def lead_details(request,pk):
    lead_detail = Lead.objects.get(id = pk)
    context ={
        'lead':lead_detail
    }
    print(lead_detail)
    return render(request, 'leads/lead_detail.html', context)

###########################################

class LeadCreateView(LoginRequiredMixin,generic.CreateView):
    template_name   = 'leads/lead_create.html'
    form_class      = forms.LeadModelForm
    
    def get_success_url(self): #if form is save
        return reverse("leads:lead_list")

    def form_valid(self, form):
        send_mail(
            subject='A leed has been created',
            message='Go to the side to see your lead',
            from_email='mondaysolomon01@gmail.com',
            recipient_list=['mondaysolomon02@gmail.com','monday_solomon@yahoo.com']
        )
        return super(LeadCreateView, self).form_valid(form)


def lead_create(request):
    form = forms.LeadModelForm()
    if request.method == "POST":
        form = forms.LeadModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')
    context = {
        'form':form    
    }
    return render(request, 'leads/lead_create.html', context)

#since modeform is used, form.save() will do the work of line 30 downwards
##############################################
class LeadUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name   = 'leads/lead_update.html'
    form_class      = forms.LeadModelForm
    queryset        = Lead.objects.all()
    def get_success_url(self): #if form is save
        return redirect("leads:lead_list")



def lead_update(request,pk):
    lead_detail     =   Lead.objects.get(id = pk)
    form            =   forms.LeadModelForm(instance=lead_detail)
    if request.method == "POST":
        form = forms.LeadModelForm(request.POST, instance=lead_detail)

        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')

    context ={
        'lead':lead_detail,
        'form': form,
    }
    print(lead_detail)
    return render(request, 'leads/lead_update.html', context)

################################################

class LeadDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name   =     'leads/lead_delete.html' #requires me creating a template, but i will stick with FBV
    form_class      =      forms.LeadModelForm
    queryset        =      Lead.objects.all()
    def get_success_url(self): #if form is save
        return redirect("leads:lead_list")



def lead_delete(request, pk):
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect('/leads')