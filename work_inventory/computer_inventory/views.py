from django.shortcuts import render, redirect
from .models import Computer
from .forms import *
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return  render(request, 'index.html')

def display_computers(request):
    items = Computer.objects.all()#graps all the models in models

    paginator = Paginator(items, 13)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'items' : items,
        'header' :  "Computers",




    }
    return render(request,'index.html', context )#accepts 3 arguments, template ex index.html

def add_computer(request):
    if request.method == "POST":
        form = ComputersForms(request.POST)
        if form.is_valid():
            form.save()

            return redirect('display_computers')
    else:
        form = ComputersForms()
        return render(request, 'add_new.html', {'form' : form})

# def page_list(request):
#     computer_list = Computer.objects.all()
#     paginator = Paginator(computer_list, 30)
#     page = request.GET.get('page')
#     computer_list = paginator.get_page(page)
#     return  render(request, 'index.html',  {'computer_list': computer_list})

class SearchResults(ListView):
    paginate_by = 13
    model = Computer
    template_name = 'computer_list.html'



    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Computer.objects.filter(Q(computer_name__icontains=query) |
                                       Q(serial_number__icontains=query) | Q(user_name__icontains=query) |
                                       Q(person_full_name__icontains=query) |Q(location__icontains=query)|
                                       Q(operating_system__contains=query))

    def get_context_data(self,  **kwargs):
        context = super(SearchResults, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q','')
        return context

