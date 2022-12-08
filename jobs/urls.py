from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobsHomePage.as_view(), name='jobs'),
    path('jobs/<int:pk>', views.JobsDetailView.as_view(), name='jobs_detail'),
    path('jobs/<int:pk>/update/', views.JobsUpdateView.as_view(), name='jobs_update'),
    path('jobs/new/', views.JobsCreate.as_view(), name='jobs_new'),
    path('jobs/<int:pk>/delete/', views.JobsDeleteView.as_view(), name='jobs_delete'),
    # path('pdf/<int:pk>', views.job_render_pdf_view, name='pdf_job_view'),

    path('equipment_jobs/', views.EquipmentJobsHomePage.as_view(), name='equipment_jobs'),
    path('equipment_jobs/<int:pk>', views.EquipmentJobsDetailView.as_view(), name='equipment_jobs_detail'),
    path('equipment_jobs/<int:pk>/update/', views.EquipmentJobsUpdateView.as_view(), name='equipment_jobs_update'),
    path('equipment_jobs/new/', views.EquipmentJobsCreate.as_view(), name='equipment_jobs_new'),
    path('equipment_jobs/<int:pk>/delete/', views.EquipmentJobsDeleteView.as_view(), name='equipment_jobs_delete'),
]
