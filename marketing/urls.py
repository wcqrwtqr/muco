from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketingView.as_view(), name='market'),
    path('market/<int:pk>', views.marketingDetailView.as_view(), name='market_detail'),
    path('market/<int:pk>/update/', views.marketingUpdateView.as_view(), name='market_update'),
    path('market/new/', views.marketingCreateView.as_view(), name='market_new'),
    path('market/<int:pk>/delete/', views.marketingDeleteView.as_view(), name='market_delete'),
    path('pdf/<int:pk>', views.marketing_render_pdf_view, name='pdf_market_view'),

]
