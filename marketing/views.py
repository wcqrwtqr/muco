from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from marketing.models import marketingdb

# from equipmenMaintenance.models import Maintenancedb
from marketing.forms import marketingForm
from marketing.filters import marketingfilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404


class marketingView(PermissionRequiredMixin, ListView):
    template_name = "marketing/marketing_page.html"
    permission_required = "marketing.view_marketingdb"
    model = marketingdb
    queryset = marketingdb.objects.all()
    ordering = ["meeting_date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = marketingfilter(self.request.GET, queryset=self.queryset)
        return context


class marketingDetailView(PermissionRequiredMixin, DetailView):
    template_name = "marketing/marketing_detail.html"
    permission_required = "equipmentList.view_equipmentdb"
    queryset = marketingdb.objects.all()
    context_object_name = "marketing_detail"
    # TODO add more functionality
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     mypk = self.kwargs['pk'] # this will get the pk for the asset
    #     context['equipMain'] = marketingdb.objects.filter(asset=mypk)
    #     return context


class marketingUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = marketingdb
    # TODO fix the permission below
    permission_required = "equipmentList.view_equipmentdb"
    form_class = marketingForm
    template_name = "marketing/marketing_update.html"
    success_message = "%(meeting_type)s was updated successfully"
    success_url = reverse_lazy("market")


class marketingCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "is_superuser"
    template_name = "marketing/marketing_new.html"
    form_class = marketingForm
    model = marketingdb
    success_message = "New meeting was created successfully"
    success_url = reverse_lazy("market")

    def from_valid(self, form):
        """
        Validate the form before saving
        """
        self.object = form.save(commit=True)
        self.object = save()
        return super().form_valid(form)


class marketingDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = ("is_superuser",)
    model = marketingdb
    success_url = reverse_lazy("market")
    success_message = "Meeting was deleted successfully"
    template_name = "marketing/marketing_confirm_delete.html"


def marketing_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get("pk")
    marketing = get_object_or_404(marketingdb, pk=pk)
    market = marketingdb.objects.filter(pk=pk)
    template_path = "marketing/marketing_pdf.html"
    context = {
        "market": market,
    }
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
