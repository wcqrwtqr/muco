from django.urls import path
from . import views

urlpatterns = [
    path('', views.personnelListView.as_view(), name='personnel'),
    path('personnel/<int:pk>', views.personnelDetailView.as_view(), name='personnel_detail'),
    path('personnel/<int:pk>/update/', views.personnelUpdateView.as_view(), name='personnel_update'),
    path('personnel/new/', views.personnelCreateView.as_view(), name='personnel_new'),
    path('equipment/<int:pk>/delete/', views.personnelDeleteView.as_view(), name='personnel_delete'),
    # path('pdf/<int:pk>', views.equipment_render_pdf_view,
    #                       name='equipment_pdf'),
    # path('equipment/maintenace/', views.EquipmentMaintenanceListView.as_view(), name='equipment_maintenance_detail'),
]
