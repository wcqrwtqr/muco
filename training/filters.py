from .models import trainingdb
import django_filters


class trainingFilter(django_filters.FilterSet):
    CHOICES = [
        ("ascending", "Ascending"),
        ("descending", "Descending"),
    ]
    ordering = django_filters.ChoiceFilter(
        label="Ordering", choices=CHOICES, method="filter_by_order"
    )

    class Meta:
        model = trainingdb
        # labels= {
        #     'lastdayops':'Last 24hr ops',
        # }
        fields = {
            "training_name": ["icontains"],
            "training_type": ["icontains"],
            "description": ["icontains"],
        }

    def filter_by_order(self, queryset, _, value):
        expression = (
            "training_date_start" if value == "ascending" else "-training_date_start"
        )
        return queryset.order_by(expression)
