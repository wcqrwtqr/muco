from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import  login_required
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .filters import DailyreportFilter
from .forms import DailyForm
from . import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template

class DailyReportListView(PermissionRequiredMixin, ListView):
    template_name = 'dailyreport/dailyreport_page.html'
    permission_required  = "dailyreport.view_dailyreportdb"
    model = models.dailyreportdb # new
    ordering = ['operationdate']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DailyreportFilter(self.request.GET, queryset=self.queryset)
        return context

class DailyreportCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView ):
    template_name = 'dailyreport/dailyreport_new.html'
    form_class = DailyForm
    permission_required  = "dailyreport.view_dailyreportdb"
    model = models.dailyreportdb
    success_message = "%(jobid)s was crated successfully"
    success_url = reverse_lazy('dailyreport')

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)

class DailyreportDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'dailyreport/dailyreport_detail.html'
    permission_required  = "dailyreport.view_dailyreportdb"
    queryset = models.dailyreportdb.objects.all()
    context_object_name = 'dailyreport_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DailyreportUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'dailyreport/dailyreport_update.html'
    permission_required  = "dailyreport.view_dailyreportdb"
    model = models.dailyreportdb
    success_url = reverse_lazy('dailyreport')
    success_message = "%(jobid)s was updated successfully"
    # form_class = DailyForm
    fields = "__all__"   # when adding the form_class then no need for this line

class DailyreportDeleteView(PermissionRequiredMixin,SuccessMessageMixin,  DeleteView):
    permission_required = ("is_superuser", )
    model = models.dailyreportdb
    success_url = reverse_lazy('dailyreport')
    success_message = "Daily report record was deleted"
    template_name = 'dailyreport/dailyreport_confirm_delete.html'

def dailyreport_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    dailyreport = get_object_or_404(models.dailyreportdb, pk=pk)
    template_path = 'dailyreport/dailyreport_pdf.html'
    context = {'dailyreport': dailyreport}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
