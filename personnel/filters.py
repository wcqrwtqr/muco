import django_filters
from .models import personneldb


class Personnelfilter(django_filters.FilterSet):
    CHOICES = [
        ("ascending", "Ascending"),
        ("descending", "Descending"),
    ]
    ordering = django_filters.ChoiceFilter(
        label="Ordering", choices=CHOICES, method="filter_by_order"
    )

    class Meta:
        model = personneldb
        fields = {
            "first_name": ["icontains"],
            "last_name": ["icontains"],
            "position": ["icontains"],
            "department": ["icontains"],
        }

    def filter_by_order(self, queryset, _, value):
        expression = "first_name" if value == "ascending" else "-first_name"
        return queryset.order_by(expression)
