from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myapp.views import home, get_data_inserted, debug_view, get_metrics, health_check
from myproject import settings

urlpatterns = ([
                   path('api/', include('myapp.urls')),
                   path('admin/', admin.site.urls),
                   path('', home, name='home'),
                   path('', include('django_prometheus.urls')),
                   path('data/', get_data_inserted),
                   path('debug/', debug_view),
                   path('custom-metrics/', get_metrics),
                   path('health/', health_check, name='health_check'),
               ])
