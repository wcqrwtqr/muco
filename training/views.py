from django.db.models import query
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django import forms
from .forms import trainingForm
from training.models import trainingdb
from personnel.models import personneldb
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from personnel.models import personneldb
# from .filters import EquipmentFilter, EquipmentMaintenanceFilter
# from .filters import EquipmentFilter
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


class trainingListView(PermissionRequiredMixin, ListView):
    template_name = 'training/training_page.html'
    model = trainingdb
    queryset = trainingdb.objects.all()
    permission_required = 'training.view_trainingdb'




class trainingDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'training/training_detail.html'
    queryset = trainingdb.objects.all()
    context_object_name = 'training_detail'
    permission_required = 'training.view_trainingdb'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mypk = self.kwargs['pk'] # this will get the pk for the asset
        context['trainvsperson'] = trainingdb.objects.filter(id=mypk)
        return context


class trainingCreateView(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = ("is_superuser", 'training.add_trainingdb')
    template_name = 'training/training_new.html'
    form_class = trainingForm
    model = trainingdb
    success_message = "New training was created successfully"
    success_url = reverse_lazy('training')

    def from_valid(self,form):
        '''
        Validate the form before saving
        '''
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)


class trainingUpdateView(PermissionRequiredMixin ,SuccessMessageMixin,UpdateView):
    model = trainingdb
    fields = "__all__"
    success_url = reverse_lazy('training')
    permission_required = ('training.view_trainingdb')
    template_name = 'training/training_update.html'
    success_message = "%(training_type)s was updated successfully"

class trainingDeleteView(SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
    permission_required = ("is_superuser")
    template_name = 'training/training_confirm_delete.html'
    model = trainingdb
    success_url = reverse_lazy('training')
    success_message = "Training record was deleted"
