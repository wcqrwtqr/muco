from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from batteryList.models import batterydb
from equipmenMaintenance.models import Batterymaintenancedb
from batteryList.forms import BatteryForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class BatteryListView(PermissionRequiredMixin, ListView):
    template_name = 'batteryList/battery_page.html'
    permission_required = ('batteryList.view_batterydb')
    model = batterydb # new
    queryset = batterydb.objects.all()
    ordering = ['serial_num']
    def get_ordering(self):
        ordering = self.request.GET.get('ordering','serial_num') #Order live feed events according to closest start date events at the top
        return ordering


class BatteryDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'batteryList/battery_detail.html'
    queryset = batterydb.objects.all()
    permission_required = ('batteryList.view_batterydb')
    context_object_name = 'battery_detail'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mypk = self.kwargs['pk'] # this will get the pk for the asset
        context['batteryMain'] = Batterymaintenancedb.objects.filter(battery=mypk)
        return context

class BatteryUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = batterydb
    permission_required = ('batteryList.view_batterydb')
    fields = '__all__'
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
