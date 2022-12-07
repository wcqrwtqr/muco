from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,ListView,DetailView, View, CreateView, DeleteView, UpdateView
from .models import jobsdb , equipment_job_activitiesdb
from dailyreport.models import dailyreportdb
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

class JobsHomePage(PermissionRequiredMixin,ListView):
    template_name = 'jobs/jobs_page.html'
    model = jobsdb
    permission_required = ('jobs.view_jobsdb')
    queryset = jobsdb.objects.all()
    ordering = ['startDate']
    def get_ordering(self):
        ordering = self.request.GET.get('ordering','-startDate')
        return ordering

    # paginate_by = 50

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = Jobsfilter(self.request.GET, queryset=self.queryset)
    #     return context

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     filter_jobs = Jobsfilter(self.request.GET, queryset=qs)
    #     return filter_jobs.qs

class EquipmentJobsHomePage(PermissionRequiredMixin, ListView):
    template_name = 'jobs/equipment_jobs_page.html'
    permission_required = ('jobs.view_jobsdb')
    model = equipment_job_activitiesdb
    queryset = equipment_job_activitiesdb.objects.all()
    # paginate_by = 50

class JobsCreate(PermissionRequiredMixin, SuccessMessageMixin,CreateView ):
    permission_required = ("is_superuser", "jobs.add_jobsdb")
    template_name = 'jobs/jobs_new.html'
    form_class = JobsForm
    model = models.jobsdb
    success_message = "%(jobid)s was created successfully"
    success_url = reverse_lazy('jobs')

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)

class EquipmentJobsCreate(PermissionRequiredMixin, SuccessMessageMixin,CreateView ):
    permission_required = ("is_superuser")
    template_name = 'jobs/equipment_jobs_new.html'
    form_class = EquipmentJobsForm
    model = models.equipment_job_activitiesdb
    success_message = "%(jobidnew)s was created successfully"
    success_url = reverse_lazy('equipment_jobs')

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)


class JobsDetailView(PermissionRequiredMixin, DetailView):
    queryset = jobsdb.objects.all()
    permission_required = ('jobs.view_jobsdb')
    context_object_name = 'jobs_detail'
    template_name = 'jobs/jobs_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mypk = self.kwargs['pk'] # this will get the pk for the asset
        context['jobDaily'] = dailyreportdb.objects.filter(jobid=mypk)
        return context

class EquipmentJobsDetailView(PermissionRequiredMixin, DetailView):
    queryset = equipment_job_activitiesdb.objects.all()
    context_object_name = 'equipment_jobs_detail'
    permission_required = "jobs.view_equipment_job_activitiesdb"
    template_name = 'jobs/equipment_jobs_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     mypk = self.kwargs['pk'] # this will get the pk for the asset
    #     context['jobDaily'] = dailyreportdb.objects.filter(jobid=mypk)
    #     return context

class JobsUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'jobs/jobs_update.html'
    permission_required = ('jobs.view_jobsdb')
    model = models.jobsdb
    success_url = reverse_lazy('jobs')
    success_message = "%(jobid)s was updated successfully"
    fields = "__all__"

class EquipmentJobsUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'jobs/equipment_jobs_update.html'
    permission_required = "jobs.view_equipment_job_activitiesdb"
    model = models.equipment_job_activitiesdb
    success_url = reverse_lazy('equipment_jobs')
    success_message = "%(jobidnew)s was updated successfully"
    fields = "__all__"

class JobsDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = ("is_superuser")
    template_name = 'jobs/jobs_confirm_delete.html'
    model = models.jobsdb
    success_message = "Jobs record was deleted"
    success_url = reverse_lazy('jobs')
