import django_filters
from .models import equipmentdb


class Equipmentfilter(django_filters.FilterSet):
    CHOICES = [
        ("ascending", "Ascending"),
        ("descending", "Descending"),
    ]
    ordering = django_filters.ChoiceFilter(
        label="Ordering", choices=CHOICES, method="filter_by_order"
    )

    class Meta:
        model = equipmentdb
        fields = {
            "description": ["icontains"],
            "serial_num": ["icontains"],
            "departement": ["icontains"],
        }

    def filter_by_order(self, queryset, _, value):
        expression = "serial_num" if value == "ascending" else "-serial_num"
        return queryset.order_by(expression)
