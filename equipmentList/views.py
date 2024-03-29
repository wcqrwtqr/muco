from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from equipmentList.models import equipmentdb
from equipmenMaintenance.models import Maintenancedb
from equipmentList.forms import EquipmentForm
from equipmentList.filters import Equipmentfilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404


class EquipmentListView(PermissionRequiredMixin, ListView):
    template_name = "equipmentList/equipment_page.html"
    permission_required = "equipmentList.view_equipmentdb"
    model = equipmentdb
    queryset = equipmentdb.objects.all()
    ordering = ["acquisition_date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = Equipmentfilter(self.request.GET, queryset=self.queryset)
        return context


class EquipmentDetailView(PermissionRequiredMixin, DetailView):
    template_name = "equipmentList/equipment_detail.html"
    permission_required = "equipmentList.view_equipmentdb"
    queryset = equipmentdb.objects.all()
    context_object_name = "equipment_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mypk = self.kwargs["pk"]  # this will get the pk for the asset
        context["equipMain"] = Maintenancedb.objects.filter(asset=mypk)
        return context


class EquipmentUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = equipmentdb
    permission_required = "equipmentList.view_equipmentdb"
    # fields = '__all__'
    form_class = EquipmentForm
    template_name = "equipmentList/equipment_update.html"
    success_message = "%(serial_num)s Asset was deleted successfully"
    success_url = reverse_lazy("equipment")


class EquipmentCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "is_superuser"
    template_name = "equipmentList/equipment_new.html"
    form_class = EquipmentForm
    model = equipmentdb
    success_message = "New Asset was created successfully"
    success_url = reverse_lazy("equipment")

    def from_valid(self, form):
        """
        Validate the form before saving
        """
        self.object = form.save(commit=True)
        self.object = save()
        return super().form_valid(form)


class EquipmentDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = ("is_superuser",)
    model = equipmentdb
    success_url = reverse_lazy("equipment")
    success_message = "Asset was deleted successfully"
    template_name = "equipmentList/equipment_confirm_delete.html"


def equipment_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get("pk")
    equipment = get_object_or_404(equipmentdb, pk=pk)
    # equipMain = get_list_or_404(Maintenancedb, asset=pk)
    equipMain = Maintenancedb.objects.filter(asset=pk)
    template_path = "equipmentList/equipment_pdf.html"
    context = {"equipment": equipment, "equipMain": equipMain}
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response
