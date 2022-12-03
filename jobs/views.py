from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,ListView,DetailView, View, CreateView, DeleteView, UpdateView
from .models import jobsdb
# from dailyreport.models import DailyreportDB
# from django.contrib.auth.decorators import login_required
from django.urls import  reverse_lazy
from .forms import *
from .import models
# from .filters import Jobsfilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Below are the imports for the xhtml2pdf
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from django.contrib.staticfiles import finders


# Create your views here.

class JobsHomePage(ListView):
    template_name = 'jobs/jobs_page.html'
    model = jobsdb
    queryset = jobsdb.objects.all()
    # paginate_by = 50

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = Jobsfilter(self.request.GET, queryset=self.queryset)
    #     return context

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     filter_jobs = Jobsfilter(self.request.GET, queryset=qs)
    #     return filter_jobs.qs

class JobsCreate(PermissionRequiredMixin, SuccessMessageMixin,CreateView ):
    permission_required = ("is_superuser")
    template_name = 'jobs/jobs_new.html'
    form_class = JobsForm
    model = models.jobsdb
    success_message = "%(jobid)s was created successfully"
    success_url = reverse_lazy('jobs')

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)

class JobsDetailView(DetailView):
    queryset = jobsdb.objects.all()
    context_object_name = 'jobs_detail'
    template_name = 'jobs/jobs_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         mypk = self.kwargs['pk'] # this will get the pk for the asset
#         context['jobDaily'] = DailyreportDB.objects.filter(jobid=mypk)
#         return context

class JobsUpdateView( SuccessMessageMixin, UpdateView):
    template_name = 'jobs/jobs_update.html'
    model = models.jobsdb
    success_url = reverse_lazy('jobs')
    success_message = "%(jobid)s was updated successfully"
    fields = "__all__"

class JobsDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = ("is_superuser")
    template_name = 'jobs/jobs_confirm_delete.html'
    model = models.jobsdb
    success_message = "Jobs record was deleted"
    success_url = reverse_lazy('jobs')
