from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    # path('login/', views.Login.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('equipmentList/', include('equipmentList.urls')),
    path('personnel/', include('personnel.urls')),
    path('supermarket/', include('supermarket.urls')),
    path('training/', include('training.urls')),
    path('equipmenMaintenance/', include('equipmenMaintenance.urls')),
    path('jobs/', include('jobs.urls')),
    path('dailyreport/', include('dailyreport.urls')),
    path('batteryList/', include('batteryList.urls')),
    path('marketing', include('marketing.urls')),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
