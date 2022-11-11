from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    # path('login/', views.Login.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('equipmentList/', include('equipmentList.urls')),
    path('personnel/', include('personnel.urls')),
    path('equipmenMaintenance/', include('equipmenMaintenance.urls')),
]
