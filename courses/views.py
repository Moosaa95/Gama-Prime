from django.shortcuts import render
from django.views import generic
from .models import Programming, Business, Design, Management
# Create your views here.



def course_to_display(request):
    """ 
        course to display on the index page
    """
    return {
        'programming': Programming.objects.all(),
    }

# def course_index(request):
#     """ 
#         course index page
#     """
#     return render(request, 'base.html', context=course_to_display(request))


class ProgrammingListView(generic.ListView):
    """ 
        programming course list view
    """
    model = Programming
    template_name = 'courses/programming_list.html'
    context_object_name = 'programming_list'
    paginate_by = 5

class ProgrammingDetailView(generic.DetailView):
    """ 
        programming course detail view
    """
    model = Programming
    template_name = 'courses/programming_detail.html'
    context_object_name = 'programming'

class ProgrammingUpdateView(generic.UpdateView):
    """ 
        programming course update view
    """
    model = Programming
    template_name = 'courses/programming_update.html'
    fields = ['name', 'description', 'image', 'is_enroll']
    success_url = '/courses/programming/'


class ProgrammingDeleteView(generic.DeleteView):
    """ 
        programming course delete view
    """
    model = Programming
    template_name = 'courses/programming_delete.html'
    success_url = '/courses/programming/'


class DesignListView(generic.ListView):
    """ 
        design course list view
    """
    model = Design

    template_name = 'courses/design_list.html'
    context_object_name = 'designings'
    paginate_by = 5

class DesignDetailView(generic.DetailView):
    """ 
        design course detail view
    """
    model = Design
    template_name = 'courses/design_detail.html'
    context_object_name = 'designings'

class DesignUpdateView(generic.UpdateView):
    """ 
        design course update view
    """
    model = Design
    template_name = 'courses/design_update.html'
    fields = ['name', 'description', 'image', 'is_enroll']
    success_url = '/courses/design/'

class DesignDeleteView(generic.DeleteView):
    """ 
        design course delete view
    """
    model = Design
    template_name = 'courses/design_delete.html'
    success_url = '/courses/design/'




def take_course(request):
    """ 
        take course page
    """
    return render(request, 'courses/takeCourse.html')
class BusinessListView(generic.ListView):
    """ 
        business course list view
    """
    model = Business
    template_name = 'courses/business_list.html'
    context_object_name = 'businesses'
    paginate_by = 5

class BusinessDetailView(generic.DetailView):
    """ 
        business course detail view
    """
    model = Business
    template_name = 'courses/business_detail.html'
    context_object_name = 'businesses'

class BusinessUpdateView(generic.UpdateView):
    """ 
        business course update view
    """
    model = Business
    template_name = 'courses/business_update.html'
    fields = ['name', 'description', 'image', 'is_enroll']
    success_url = '/courses/business/'

class BusinessDeleteView(generic.DeleteView):
    """ 
        business course delete view
    """
    model = Business
    template_name = 'courses/business_delete.html'
    success_url = '/courses/business/'


class ManagementListView(generic.ListView):
    """ 
        management course list view
    """
    model = Management
    template_name = 'courses/management_list.html'
    context_object_name = 'management'
    paginate_by = 5

class ManagementDetailView(generic.DetailView):
    """ 
        management course detail view
    """
    model = Management
    template_name = 'courses/management_detail.html'
    context_object_name = 'management'


class ManagementUpdateView(generic.UpdateView):
    """ 
        management course update view
    """
    model = Management
    template_name = 'courses/management_update.html'
    fields = ['name', 'description', 'image', 'is_enroll']
    success_url = '/courses/management/'

class ManagementDeleteView(generic.DeleteView):
    """ 
        management course delete view
    """
    model = Management
    template_name = 'courses/management_delete.html'
    success_url = '/courses/management/'