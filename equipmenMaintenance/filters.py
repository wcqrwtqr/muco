from django.core.checks import register
import django_filters
from .models import Maintenancedb , Batterymaintenancedb



class Maintenancefilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = Maintenancedb
        fields = {
            'description' : ['icontains'],
            'ms_type' : ['icontains'],
        }

    def filter_by_order(self,queryset, _, value):
        expression  = 'main_date_start' if value == 'ascending' else  '-main_date_start'
        return queryset.order_by(expression)

class BatteryMaintenancefilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = Batterymaintenancedb
        fields = {
            'description' : ['icontains'],
            'ms_type' : ['icontains'],
        }

    def filter_by_order(self,queryset, _, value):
        expression  = 'check_date' if value == 'ascending' else  '-check_date'
        return queryset.order_by(expression)
