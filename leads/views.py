from django.shortcuts import redirect, render
from . models import Agent, Lead
from . import forms

# Create your views here.
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
    form = forms.LeadForm()
    if request.method == "POST":
        form = forms.LeadForm(request.POST)
        print('YOu have a post method')

        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['first_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.order_by('?')[0]
            Lead.objects.create(
               first_name = first_name,
               last_name =  last_name,
               age = age,
               agent = agent
            )
            print('leads created')
            return redirect('home')
    context = {
        'form':forms.LeadForm()
    
    }
    return render(request, 'leads/lead_create.html', context)