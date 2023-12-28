import django_filters
from .models import jobsdb


class Jobsfilter(django_filters.FilterSet):
    CHOICES = [
        ("ascending", "Ascending"),
        ("descending", "Descending"),
    ]
    ordering = django_filters.ChoiceFilter(
        label="Ordering", choices=CHOICES, method="filter_by_order"
    )

    class Meta:
        model = jobsdb
        # fields  ="__all__"
        fields = {
            # 'JOBID' : ['icontains'], removed the unwanted fields for a smaller filter set
            "client": ["icontains"],
            "well": ["icontains"],
            "departmenet": ["icontains"],
            "service": ["icontains"],
        }

    def filter_by_order(self, queryset, name, value):
        expression = "startDate" if value == "ascending" else "-startDate"
        return queryset.order_by(expression)
