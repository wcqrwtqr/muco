from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View, CreateView
from .models import Maintenancedb
from django.urls import  reverse_lazy
# from .forms import MaintenanceForm
# from .filters import Maintenancefilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class MaintenanceHomePage(ListView):
    template_name = 'equipmenMaintenance/maintenance_page.html'
    queryset = Maintenancedb.objects.all()
    model = Maintenancedb
    # paginate_by = 50

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = Maintenancefilter(self.request.GET, queryset=self.queryset)
    #     return context

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     filter_maintenance = Maintenancefilter(self.request.GET, queryset=qs)
    #     return filter_maintenance.qs

class MaintenanceDetailView(DetailView):
    queryset = Maintenancedb.objects.all()
    template_name = 'equipmenMaintenance/maintenance_detail.html'
    context_object_name = 'maintenance_detail'

# class MaintenanceCreate(SuccessMessageMixin,CreateView ):
# class MaintenanceCreate(CreateView ):
#     template_name = 'equipmenMaintenance/maintenance_new.html'
#     # form_class = MaintenanceForm
#     model = Maintenancedb
#     success_url = reverse_lazy('maintenance')
#     # success_message = "%(ms_type)s was created successfully"

#     def from_valid(self, form):
#         self.object = form.save(commit = True)
#         self.object = save()
#         # success_message = "Maintenance created"
#         return super().form_valid(form)
