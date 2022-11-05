from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from equipmentList.models import equipmentdb
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.

class EquipmentListView(ListView):

    template_name = 'equipmentList/equipment_page.html'
    model = equipmentdb # new
    queryset = equipmentdb.objects.all()
    # paginate_by = 50

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = EquipmentFilter(self.request.GET, queryset=self.queryset)
    #     # Below context is for select2 dropdown list searchablity
    #     # context['full_list'] = models.EQUIPMENT_DB.objects.all()
    #     return context

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     filter_equipment = EquipmentFilter(self.request.GET, queryset=qs)
    #     return filter_equipment.qs



class EquipmentDetailView(DetailView):
    template_name = 'equipmentList/equipment_detail.html'
    queryset = equipmentdb.objects.all()
    context_object_name = 'equipment_detail'
    # print(queryset)
# def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     mypk = self.kwargs['pk'] # this will get the pk for the asset
    #     context['equipMain'] = MaintenanceDB.objects.filter(asset=mypk)
    #     return context



class EquipmentUpdateView(SuccessMessageMixin,UpdateView):
    model = equipmentdb
    fields = '__all__'
    template_name = 'equipmentList/equipment_update.html'
    success_message = "%(serial_num)s Asset was deleted successfully"
    success_url = reverse_lazy('equipment')