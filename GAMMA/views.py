from multiprocessing import context
from courses.models import Programming, Business, Design, Management
from django.shortcuts import render




def to_display(request):
    """ 
         to display on the index page
    """
    return {
        'programming': Programming.objects.all(),
    }

def  index(request):
    """ 
        course index page
    """
    return render(request, 'base.html', context=to_display(request))
