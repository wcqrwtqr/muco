from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
    CreateView,
)
from .models import Maintenancedb, Batterymaintenancedb
from django.urls import reverse_lazy
from .forms import MaintenanceForm, BatteryMaintenanceForm
from .filters import BatteryMaintenancefilter, Maintenancefilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Battery section


class MaintenanceHomePage(PermissionRequiredMixin, ListView):
    template_name = "equipmenMaintenance/maintenance_page.html"
    queryset = Maintenancedb.objects.all()
    model = Maintenancedb
    permission_required = "equipmenMaintenance.view_maintenancedb"
    ordering = ["main_date_start"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = Maintenancefilter(self.request.GET, queryset=self.queryset)
        return context


class MaintenanceDetailView(PermissionRequiredMixin, DetailView):
    queryset = Maintenancedb.objects.all()
    permission_required = "equipmenMaintenance.view_maintenancedb"
    template_name = "equipmenMaintenance/maintenance_detail.html"
    context_object_name = "maintenance_detail"


class MaintenanceCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "equipmenMaintenance/maintenance_new.html"
    form_class = MaintenanceForm
    model = Maintenancedb
    permission_required = "equipmenMaintenance.add_maintenancedb"
    success_url = reverse_lazy("maintenance")
    success_message = "%(ms_type)s was created successfully"

    def from_valid(self, form):
        self.object = form.save(commit=True)
        self.object = save()
        return super().form_valid(form)


class MaintenanceUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Maintenancedb
    form_class = MaintenanceForm
    success_url = reverse_lazy("maintenance")
    template_name = "equipmenMaintenance/maintenance_update.html"
    permission_required = "equipmenMaintenance.change_maintenancedb"
    success_message = "%(asset)s was updated successfully"


class MaintenanceDeleteView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ("is_superuser", "equipmenMaintenance.delete_maintenancedb")
    template_name = "equipmenMaintenance/maintenance_confirm_delete.html"
    model = Maintenancedb
    success_url = reverse_lazy("maintenance")
    success_message = "Main record was deleted"


# Battery section


class BatteryMaintenanceHomePage(PermissionRequiredMixin, ListView):
    template_name = "equipmenMaintenance/battery_maintenance_page.html"
    model = Batterymaintenancedb
    queryset = Batterymaintenancedb.objects.all()
    permission_required = "equipmenMaintenance.view_maintenancedb"
    ordering = ["check_date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = BatteryMaintenancefilter(
            self.request.GET, queryset=self.queryset
        )
        # This is an option to select the light or dark drop down list for the action button
        context["class_drop"] = {
            "dark": "dropdown-menu-dark",
            "light": "dropdown-menu-light",
        }
        return context


class BatteryMaintenanceDetailView(PermissionRequiredMixin, DetailView):
    queryset = Batterymaintenancedb.objects.all()
    permission_required = "equipmenMaintenance.view_batterymaintenancedb"
    template_name = "equipmenMaintenance/battery_maintenance_detail.html"
    context_object_name = "battery_maintenance_detail"


class BatteryMaintenanceCreate(
    PermissionRequiredMixin, SuccessMessageMixin, CreateView
):
    template_name = "equipmenMaintenance/battery_maintenance_new.html"
    form_class = BatteryMaintenanceForm
    model = Batterymaintenancedb
    permission_required = "equipmenMaintenance.add_maintenancedb"
    success_url = reverse_lazy("battery_maintenance")
    success_message = "%(ms_type)s was created successfully"

    def from_valid(self, form):
        self.object = form.save(commit=True)
        self.object = save()
        # success_message = "Maintenance created"
        return super().form_valid(form)


class BatteryMaintenanceUpdateView(
    PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Batterymaintenancedb
    # fields = "__all__"
    form_class = BatteryMaintenanceForm
    success_url = reverse_lazy("battery_maintenance")
    template_name = "equipmenMaintenance/battery_maintenance_update.html"
    permission_required = "equipmenMaintenance.change_maintenancedb"
    success_message = "%(battery)s was updated successfully"


class BatteryMaintenanceDeleteView(
    SuccessMessageMixin, PermissionRequiredMixin, DeleteView
):
    permission_required = ("is_superuser", "equipmenMaintenance.delete_maintenancedb")
    template_name = "equipmenMaintenance/battery_maintenance_confirm_delete.html"
    model = Batterymaintenancedb
    success_url = reverse_lazy("battery_maintenance")
    success_message = "battery record was deleted"
