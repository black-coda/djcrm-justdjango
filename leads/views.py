from django.shortcuts import redirect, render
from django.urls import reverse
from . models import Agent, Lead
from . import forms
from django.views import generic

# Create your views here.
class LandingView(generic.TemplateView):
    template_name = "landing.html"

def landing_page_view( request,*args, **kwargs):
    return render(request,'landing.html' ,*args, **kwargs,)
########################################

class LeadListView(generic.ListView):
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

class LeadDetailView(generic.DetailView):
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

class LeadCreateView(generic.CreateView):
    template_name   = 'leads/lead_create.html'
    form_class      = forms.LeadModelForm
    
    def get_success_url(self): #if form is save
        return reverse("leads:lead_list")


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
class LeadUpdateView(generic.UpdateView):
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

class LeadDeleteView(generic.DeleteView):
    template_name   =     'leads/lead_delete.html' #requires me creating a template, but i will stick with FBV
    form_class      =      forms.LeadModelForm
    queryset        =      Lead.objects.all()
    def get_success_url(self): #if form is save
        return redirect("leads:lead_list")



def lead_delete(request, pk):
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect('/leads')