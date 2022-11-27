from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainingListView.as_view(), name='training'),
    path('training/<int:pk>', views.trainingDetailView.as_view(), name='training_detail'),
    path('training/new/', views.trainingCreateView.as_view(), name='training_new'),
    path('training/<int:pk>/update/', views.trainingUpdateView.as_view(), name='training_update'),
    path('traininig/<int:pk>/delete/', views.trainingDeleteView.as_view(), name='training_delete'),
    # path('pdf/<int:pk>', views.equipment_render_pdf_view,
    #                       name='equipment_pdf'),
    # path('equipment/maintenace/', views.EquipmentMaintenanceListView.as_view(), name='equipment_maintenance_detail'),
]
