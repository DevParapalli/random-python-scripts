from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

from .models import ToDo
from .forms import ToDoForm
# Create your views here.
def to_do(request):
    reminder_list = ToDo.objects.order_by('-dead_line')
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do')
    form = ToDoForm()
    
    navbar_list = [
        {
            'link':reverse('index'),
            'name':'HOME'
        },
        {
            'link':reverse('to_do'),
            'name':'TO-DO'
        },
        {
            'link':"https://html5up.net/solid-state",
            'name':'TEMPLATE Details'
        }
    ]
    
    
    
    if len(reminder_list) == 0:
        reminder_list = [
            {
                "title":'No Reminders Here.',
                "data":"Start by creating one above.",
                "created_date_time":"",
                "dead_line":""
            }
        ]
    
    context = {
        'page_title':'To-Do By RogueCatalyst',
        'nav_bar':navbar_list,
        'content':{},
        'form':form.as_table(),
        'to_do_list':reminder_list,
        
    }
    
    
    return render(request, 'to_do/to_do.html', context=context)

def remove(request, identifier):
    item = ToDo.objects.get(id=identifier) 
    
    messages.info(request, "Marked {} as DONE".format(item.title)) 
    item.delete() 
    return redirect('to_do')