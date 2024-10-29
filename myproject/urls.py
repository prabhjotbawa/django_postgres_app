from django.contrib import admin
from django.urls import path, include
from myapp.views import home, get_data_inserted, debug_view, get_metrics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('django_prometheus.urls')),
    path('data/', get_data_inserted),
    path('debug/', debug_view),
    path('custom-metrics/', get_metrics)
]
