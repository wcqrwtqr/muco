from django.urls import path
from . import views

urlpatterns = [
    path('', views.BatteryListView.as_view(), name='battery'),
    path('battery/<int:pk>', views.BatteryDetailView.as_view(), name='battery_detail'),
    path('battery/<int:pk>/update/', views.BatteryUpdateView.as_view(), name='battery_update'),
    path('battery/new/', views.BatteryCreateView.as_view(), name='battery_new'),
    path('battery/<int:pk>/delete/', views.BatteryDeleteView.as_view(), name='battery_delete'),
    path('pdf/<int:pk>', views.battery_render_pdf_view, name='battery_pdf'),
]
