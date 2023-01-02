import django_filters
from .models import marketingdb

class marketingfilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')
    class Meta:
        model  = marketingdb
        # fields  ="__all__"
        fields = {
            'client' : ['icontains'],
            'departement' : ['icontains'],
        }

    def filter_by_order(self,queryset,name, value):
        expression  = 'meeting_date' if value == 'ascending' else  '-meeting_date'
        return queryset.order_by(expression)
