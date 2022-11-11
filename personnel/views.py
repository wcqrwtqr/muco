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
# from equipmentMaintenance.models import MaintenanceDB
from personnel.models import personneldb
# from .filters import EquipmentFilter, EquipmentMaintenanceFilter
# from .filters import EquipmentFilter
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


class personnelListView(ListView):

    template_name = 'personnel/personnel_page.html'
    # queryset = models.EQUIPMENT_DB.objects.all()
    model = personneldb
    queryset = personneldb.objects.all()
    # paginate_by = 50

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = EquipmentFilter(self.request.GET, queryset=self.queryset)
    #     # Below context is for select2 dropdown list searchablity
    #     # context['full_list'] = models.EQUIPMENT_DB.objects.all()
    #     return context

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     # filter_equipment = EquipmentFilter(self.request.GET, queryset=qs)
    #     return filter_equipment.qs


class personnelDetailView(DetailView):
    template_name = 'personnel/personnel_detail.html'
    queryset = models.personneldb.objects.all()
    context_object_name = 'personnel_detail'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     mypk = self.kwargs['pk'] # this will get the pk for the asset
    #     context['personnelMain'] = MaintenanceDB.objects.filter(asset=mypk)
    #     return context


class personnelCreateView(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = ("is_superuser")
    template_name = 'personnel/personnel_new.html'
    form_class = personnelForm
    model = personneldb
    success_message = "New Personel was created successfully"
    success_url = reverse_lazy('personnel')

    def from_valid(self,form):
        '''
        Validate the form before saving
        '''
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)


class personnelDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = ("is_superuser", )
    model = personneldb
    success_url = reverse_lazy('personnel')
    success_message = "Personel was deleted successfully"
    template_name = 'personnel/personnel_confirm_delete.html'


class personnelUpdateView(SuccessMessageMixin,UpdateView):
    model = personneldb
    fields = '__all__'
    template_name = 'personnel/personnel_update.html'
    success_message = "%(first_name)s Asset was deleted successfully"
    success_url = reverse_lazy('personnel')
