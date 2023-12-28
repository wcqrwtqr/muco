from django.shortcuts import render
from django.views.generic import ListView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import supermarketdb

# Create your views here.


class SupermarketHomePage(PermissionRequiredMixin, ListView):
    template_name = "supermarket/supermarket_page.html"
    model = supermarketdb
    permission_required = "supermarket.view_supermarketdb"
    queryset = supermarketdb.objects.all()
    ordering = ["product_name"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['filter'] = Jobsfilter(self.request.GET, queryset=self.queryset)
        return context
