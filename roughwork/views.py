from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

# from roughwork.forms import WorkshopForm
from roughwork.models import Workshop


#Custom Mixins
class WorkshopMixin(object):
    queryset = Workshop.objects.completed()


class WorkshopListView(WorkshopMixin, LoginRequiredMixin, ListView):
    template_name = 'workshops/workshop_list.html'


# CRUD - Create, Read, Update, Delete
# Create
class WorkshopCreateView(LoginRequiredMixin, CreateView):
    template_name = 'workshops/workshop_create.html'
    model = Workshop
    fields = "__all__"


# Read
class WorkshopDetailView(WorkshopMixin, LoginRequiredMixin, DetailView):
    template_name = 'workshops/workshop_detail.html'


# Update
class WorkshopUpdateView(WorkshopMixin, LoginRequiredMixin, UpdateView):
    template_name = 'workshops/workshop_create.html'
    model = Workshop
    fields = "__all__"


# Delete
class WorkshopDeleteView(WorkshopMixin, LoginRequiredMixin, DeleteView):
    # Render a template from a specific object
    template_name = 'workshops/workshop_delete.html'

    def get_success_url(self):
        return reverse('workshops:workshop-list')


# Mixins





