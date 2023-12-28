from .models import dailyreportdb
import django_filters


class DailyreportFilter(django_filters.FilterSet):
    CHOICES = [
        ("ascending", "Ascending"),
        ("descending", "Descending"),
    ]
    ordering = django_filters.ChoiceFilter(
        label="Ordering", choices=CHOICES, method="filter_by_order"
    )

    class Meta:
        model = dailyreportdb
        # labels= {
        #     'lastdayops':'Last 24hr ops',
        # }
        fields = {
            "lastdayops": ["icontains"],
        }

    def filter_by_order(self, queryset, _, value):
        expression = "operationdate" if value == "ascending" else "-operationdate"
        return queryset.order_by(expression)
