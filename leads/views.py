from django.shortcuts import redirect, render
from . models import Agent, Lead
from . import forms

# Create your views here.
def landing_page_view( request,*args, **kwargs):
    return render(request,'landing.html' ,*args, **kwargs,)

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads':leads
    }
    return render(request, 'leads/lead_list.html', context)

def lead_details(request,pk):
    lead_detail = Lead.objects.get(id = pk)
    context ={
        'lead':lead_detail
    }
    print(lead_detail)
    return render(request, 'leads/lead_detail.html', context)

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

def lead_update(request,pk):
    lead_detail = Lead.objects.get(id = pk)
    form = forms.LeadModelForm(instance=lead_detail)
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

def lead_delete(request, pk):
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect('/leads')