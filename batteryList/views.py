from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from batteryList.models import batterydb
from jobs.models import equipment_job_activitiesdb # test TODO lets check
from equipmenMaintenance.models import Batterymaintenancedb
from batteryList.forms import BatteryForm
from batteryList.filters import batteryfilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404, get_list_or_404

class BatteryListView(PermissionRequiredMixin, ListView):
    template_name = 'batteryList/battery_page.html'
    permission_required = ('batteryList.view_batterydb')
    model = batterydb # new
    queryset = batterydb.objects.all()
    ordering = ['serial_num']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = batteryfilter(self.request.GET, queryset=self.queryset)
        return context

class BatteryDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'batteryList/battery_detail.html'
    queryset = batterydb.objects.all()
    permission_required = ('batteryList.view_batterydb')
    context_object_name = 'battery_detail'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mypk = self.kwargs['pk'] # this will get the pk for the asset
        context['batteryMain'] = Batterymaintenancedb.objects.filter(battery=mypk)
        context['batteryinjob'] = equipment_job_activitiesdb.objects.filter(battery=mypk)
        return context

class BatteryUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = batterydb
    permission_required = ('batteryList.view_batterydb')
    # fields = '__all__'
    form_class = BatteryForm
    template_name = 'batteryList/battery_update.html'
    success_message = "%(serial_num)s Asset was deleted successfully"
    success_url = reverse_lazy('battery')

class BatteryCreateView(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = ("is_superuser")
    template_name = 'batteryList/battery_new.html'
    form_class = BatteryForm
    model = batterydb
    success_message = "New Batter was created successfully"
    success_url = reverse_lazy('battery')

    def from_valid(self,form):
        '''
        Validate the form before saving
        '''
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)

class BatteryDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = ("is_superuser", )
    model = batterydb
    success_url = reverse_lazy('battery')
    success_message = "Asset was deleted successfully"
    template_name = 'batteryList/battery_confirm_delete.html'

def battery_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    battery = get_object_or_404(batterydb, pk=pk)
    batteryMain = Batterymaintenancedb.objects.filter(battery=pk)
    template_path = 'batteryList/battery_pdf.html'
    context = {'battery': battery, 'batteryMain':batteryMain}
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
