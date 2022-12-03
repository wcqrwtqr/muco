from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View, CreateView
from .models import Maintenancedb, Batterymaintenancedb
from django.urls import  reverse_lazy
from .forms import MaintenanceForm, BatteryMaintenanceForm
# from .filters import Maintenancefilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class MaintenanceHomePage(PermissionRequiredMixin,ListView):
    template_name = 'equipmenMaintenance/maintenance_page.html'
    queryset = Maintenancedb.objects.all()
    model = Maintenancedb
    permission_required = 'equipmenMaintenance.view_maintenancedb'

    # paginate_by = 50

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = Maintenancefilter(self.request.GET, queryset=self.queryset)
    #     return context

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     filter_maintenance = Maintenancefilter(self.request.GET, queryset=qs)
    #     return filter_maintenance.qs

class BatteryMaintenanceHomePage(PermissionRequiredMixin,ListView):
    template_name = 'equipmenMaintenance/battery_maintenance_page.html'
    model = Batterymaintenancedb
    queryset = Batterymaintenancedb.objects.all()
    permission_required = 'equipmenMaintenance.view_maintenancedb'

class MaintenanceDetailView(DetailView):
    queryset = Maintenancedb.objects.all()
    template_name = 'equipmenMaintenance/maintenance_detail.html'
    context_object_name = 'maintenance_detail'

class BatteryMaintenanceDetailView(DetailView):
    queryset = Batterymaintenancedb.objects.all()
    template_name = 'equipmenMaintenance/battery_maintenance_detail.html'
    context_object_name = 'battery_maintenance_detail'

class MaintenanceCreate(PermissionRequiredMixin, SuccessMessageMixin,CreateView ):
    template_name = 'equipmenMaintenance/maintenance_new.html'
    form_class = MaintenanceForm
    model = Maintenancedb
    permission_required = 'equipmenMaintenance.add_maintenancedb'
    success_url = reverse_lazy('maintenance')
    success_message = "%(ms_type)s was created successfully"

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        # success_message = "Maintenance created"
        return super().form_valid(form)



class BatteryMaintenanceCreate(PermissionRequiredMixin, SuccessMessageMixin,CreateView ):
    template_name = 'equipmenMaintenance/battery_maintenance_new.html'
    form_class = BatteryMaintenanceForm
    model = Batterymaintenancedb
    permission_required = 'equipmenMaintenance.add_maintenancedb'
    success_url = reverse_lazy('battery_maintenance')
    success_message = "%(ms_type)s was created successfully"

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        # success_message = "Maintenance created"
        return super().form_valid(form)

class MaintenanceUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Maintenancedb
    fields = "__all__"
    success_url = reverse_lazy('maintenance')
    template_name = 'equipmenMaintenance/maintenance_update.html'
    permission_required = 'equipmenMaintenance.change_maintenancedb'
    success_message = "%(asset)s was updated successfully"

class BatteryMaintenanceUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Batterymaintenancedb
    fields = "__all__"
    success_url = reverse_lazy('battery_maintenance')
    template_name = 'equipmenMaintenance/battery_maintenance_update.html'
    # TODO - check this part of persmission required FIXME
    permission_required = 'equipmenMaintenance.change_maintenancedb'
    success_message = "%(battery)s was updated successfully"

class MaintenanceDeleteView(SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
    permission_required = ("is_superuser", 'equipmenMaintenance.delete_maintenancedb')
    template_name = 'equipmenMaintenance/maintenance_confirm_delete.html'
    model = Maintenancedb
    success_url = reverse_lazy('maintenance')
    success_message = "Main record was deleted"

class BatteryMaintenanceDeleteView(SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
    permission_required = ("is_superuser", 'equipmenMaintenance.delete_maintenancedb')
    template_name = 'equipmenMaintenance/battery_maintenance_confirm_delete.html'
    model = Batterymaintenancedb
    success_url = reverse_lazy('battery_maintenance')
    success_message = "battery record was deleted"
