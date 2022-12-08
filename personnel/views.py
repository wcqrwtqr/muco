from django.db.models import query
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django import forms
from .forms import personnelForm
from . import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from personnel.models import personneldb
# from .filters import EquipmentFilter, EquipmentMaintenanceFilter
# from .filters import EquipmentFilter
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


class personnelListView(PermissionRequiredMixin, ListView):

    template_name = 'personnel/personnel_page.html'
    model = personneldb
    queryset = personneldb.objects.all()
    permission_required = 'personnel.view_personneldb'
    # paginate_by = 50

class personnelDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'personnel/personnel_detail.html'
    permission_required = 'personnel.view_personneldb'
    queryset = personneldb.objects.all()
    context_object_name = 'personnel_detail'

class personnelCreateView(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    template_name = 'personnel/personnel_new.html'
    form_class = personnelForm
    model = personneldb
    permission_required = 'personnel.add_personneldb'
    success_message = "New Personel was created successfully"
    success_url = reverse_lazy('personnel')

    def from_valid(self,form):
        '''
        Validate the form before saving
        '''
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)


class personnelUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = personneldb
    fields = '__all__'
    permission_required = 'personnel.view_personneldb' # BUG  there is an issue here need to fix it as I can not
    template_name = 'personnel/personnel_update.html'
    success_message = "Record was updated successfully"
    success_url = reverse_lazy('personnel')

class personnelDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = ("is_superuser", )
    model = personneldb
    success_url = reverse_lazy('personnel')
    success_message = "Personel was deleted successfully"
    template_name = 'personnel/personnel_confirm_delete.html'
