# this is for rendering page to template 
from django.shortcuts import render

from django.urls import reverse


# Create your views here.
def index(request):
    
    content_list = [
        {
            'number':'one',
            'title':'Test for TO-DO App',
            'style':'style1',
            'image':'/images/pic01.jpg', # this is the picture used for the content. change a/c to context
            'alt_image':'Just a gradient used in development.',
            'link': reverse('to_do'),
            'link_text':'TO-DO',
            'content':'The to_do page calls you.'
        },
        {
            'number':'two',
            ''
            'title':'This is Solid State',
            'style':'alt style2', # alt should be alternately inserted into style for criss cross patterns
            'image':'/images/pic02.jpg', # this is the picture used for the content. change a/c to context
            'alt_image':'Just a gradient used in development.',
            'link': reverse('index'),
            'link_text':'LEARN MORE',
            'content':'Another free + fully responsive site template by HTML5 UP (See Nav Bar for Details.)'
        }
    ]
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
    
    
    
    context = {
        'page_title':'RogueCatalyst',
        'nav_bar':navbar_list,
        'content':content_list,
    }
    return render(request, 'index_app/index.html', context)